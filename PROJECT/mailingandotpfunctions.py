import clx.xms
import requests
import random
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl


def generateOTP():
    # Declare a string variable
    # which stores all string
    string = '0123456789'
    OTP = ""

    length = len(string)
    for i in range(random.randint(5, 7)):
        OTP += string[math.floor(random.random() * length)]

    return OTP


global comn_otp
comn_otp = generateOTP()


def send_otp_mobile():
    client = clx.xms.Client(service_plan_id='b535562ba0874242bb827e52a08a62b9',
                            token='b3cc0e51cf23498c98ae97836ce90133')
    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = '447537404817'
    create.recipients = {'918825965069'}
    create.body = comn_otp + " is the OTP"
    print(comn_otp + " in mobile")
    # result = "mobile_otp_sent"
    # return result

    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestException,
            clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))

    result = "mobile_otp_sent"
    return result


def send_otp_mail(mail_id):
    print(comn_otp + " in mail")
    # maild_id = 'arjithchandru46@gmail.com'
    # The mail addresses and password
    sender_address = 'otpbot.webservice@gmail.com'
    sender_pass = 'balaji1234'
    receiver_address = mail_id

    # print(mail_content)
    # Setup the MIME
    message = MIMEMultipart('alternative')

    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "Verification"  # The subject line
    # The body and the attachments for the mail


    mail_content = comn_otp + " is the OTP"
    message.attach(MIMEText(mail_content, 'plain'))
    message.attach(MIMEText('<html><body><h1>Hi </h1><p>this is from cinepolice, please click this to move on further processs <a href="http://127.0.0.1:5015/cinepolice/movielist">START BOOKING</a>...</p> </body></html>', 'html'))



    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()

    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    result = "OTP Sent Through mail and mobile number"
    return result


def main_fun(mail_id):
    # successmobile = send_otp_mobile()
    mail = mail_id
    successmail = send_otp_mail(mail)
    # send_otp_mobile()
    # send_otp_mail()

    return successmail

# main_fun()
# send_otp_mail()