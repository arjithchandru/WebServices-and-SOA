import flask
from flask import request, render_template, url_for
from flask_cors import CORS
from mailingandotpfunctions import *


app = flask.Flask(__name__, template_folder='template')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def error404():
    return render_template("error404.html")

@app.route('/cinepolice')
def index():
    return render_template("index.html")

@app.route('/cinepolice/verifyemail', methods=['POST'])
def login_email():
    option_value = request.form.get("opvalue")
    if (option_value == "mailing"):
        mail_id = request.form.get("mailid")
        username = request.form.get("username")
        mail = main_fun(mail_id)
        # print(mail)
        return render_template('verifymail.html',useremailadderss = mail_id, username=username, application_name="CINEPOLICE")
    elif(option_value == "mobilenumber"):
        mobile_id = request.form.get("mobilenumber")
        username = request.form.get("username")
        mail = send_otp_mobile()
        # print(mail)
        return render_template('verifyotp.html', useremailadderss=mobile_id, username=username, application_name="CINEPOLICE")
    else:
        return render_template("error404.html")

@app.route('/cinepolice/movielist')
def movielist():
    return render_template("movielist.html")

@app.route('/cinepolice/booking')
def bookingseat():
    return render_template("booking.html")


app.run(host='127.0.0.1', port = 5015)