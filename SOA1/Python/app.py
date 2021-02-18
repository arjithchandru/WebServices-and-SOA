import flask
from flask import request, render_template, jsonify, url_for
from flask_cors import CORS
import os
from PIL import Image, ImageDraw, ImageFont,ImageFilter
import PIL.ImageDraw
import PIL.Image
import base64
import pyqrcode
import png
from pyqrcode import QRCode
from barcode import EAN13
from barcode.writer import ImageWriter

from function import *


app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ftw', methods=['POST'])
def ftws():
    return render_template("Figuretowords.html")

@app.route('/otps', methods=['POST'])
def gotpss():
    return render_template("gotp.html")

@app.route('/ddf', methods=['POST'])
def ddfss():
    return render_template("datedifference.html")

@app.route('/sops', methods=['POST'])
def sopss():
    return render_template("setoperations.html")

@app.route('/matops', methods=['POST'])
def matopss():
    return render_template("matrix.html")

@app.route('/rsaops', methods=['POST'])
def rsaopss():
    return render_template("RSA.html")

@app.route('/mdhash', methods=['POST'])
def mdhashs():
    return render_template("MDhash.html")

@app.route('/gbarcode', methods=['POST'])
def barcodes():
    return render_template("barcode.html")

@app.route('/gqrcode', methods=['POST'])
def qrecodes():
    return render_template("qrcode.html")

@app.route('/gcaptcha', methods=['POST'])
def captchas():
    return render_template("captcha.html")


@app.route('/OTPgeneration', methods=['POST'])
def OTP():
    print('inside OTPgeneration')
    res = main_function()
    # return (res)
    print (res)
    output ="generated otp :" + str(res)

    # return jsonify({'name': output})
    return render_template('gotp.html', otp=output)
    # return output


@app.route('/figuretoword', methods=['POST'])
def figuretoword():
    print("inside figure to word")
    # numbers = float(request.args.get("number"))
    numbers = int(request.form.get('number'))
    main, sub = divmod(numbers, 1)
    res = figure_to_word(main,sub)
    # return (res)
    output = str(res)

    # return jsonify({'name': output})
    # return output
    return render_template('Figuretowords.html', number = numbers, res = output)

@app.route('/datediff', methods=['POST'])
def diff():
    # print('at start')
    # da1= request.form['da1']
    da1 = request.form.get("da1")
    da2 = request.form.get("da2")
    da1 = da1.split('-', 2)
    da2 = da2.split('-', 2)
    year1, month1, date1 = da1
    year2, month2, date2 = da2
    time1 = request.form.get("t1")
    time2 = request.form.get("t2")
    # print(year1, month1, date1)
    # print(year2, month2, date2)

    if date1 > date2 or month1 > month2 or year1 > year2:
        ddate = int(date1)
        dmonth = int(month1)
        dyear = int(year1)
        date1 = int(date2)
        month1 = int(month2)
        year1 = int(year2)
        date2 = int(ddate)
        month2 = int(dmonth)
        year2 = int(dyear)
    else:
        date1 = int(date1)
        month1 = int(month1)
        year1 = int(year1)
        date2 = int(date2)
        month2 = int(month2)
        year2 = int(year2)

    print(year1, month1, date1)
    print(year2, month2, date2)

    # date1 = 11
    # month1 = 2
    # year1 = 2006
    # date2 = 12
    # month2 = 2
    # year2 = 2006
    fdate = (str(da1) +" "+ str(time1))
    tdate = (str(da2) +" "+ str(time2))
    res = diff_date(date1, date2, month1, month2, year1, year2, time1, time2)
    return render_template('datedifference.html', res = res, fdate=fdate, tdate=tdate)

@app.route('/setoperations', methods=['POST'])
def setOps():
    # print(request.args)
    operation = int(request.form.get('opChoice'))
    setA = list(request.form.get('seta').split(','))
    setB = list(request.form.get('setb').split(','))
    set1 = setA
    set2 = setB

    if (operation == 0):
        op = 'union'
        result = union_op(setA, setB)
    elif(operation == 1):
        op = 'intersection'
        result = intersect_op(setA, setB)
    elif(operation == 2):
        op = 'difference'
        result = diff_op(setA, setB)


    return render_template('setoperations.html', operations = op, set1 = set1, set2 = set2, res=result)

@app.route('/matrixops', methods=['POST'])
def matrixOps():
    operation = int(request.form.get('opChoice'))
    row = int(request.form.get('row'))
    col = int(request.form.get('col'))

    matrix = map(int, request.form.get('matrix').split(','))

    tempMat = []
    matrixA = []
    colBkp = col
    for idx, key in enumerate(matrix):
        if (idx < col):
            tempMat.append(key)
        else:
            matrixA.append(tempMat)
            tempMat = []
            col += colBkp
            tempMat.append(key)
    matrixA.append(tempMat)

    print('Orgmatrix', matrixA)
    col = colBkp

    if (operation == 0):
        print([[matrixA[j][i] for j in range(len(matrixA))] for i in range(len(matrixA[0]))])
        matrixB = transpose(matrixA, row, col)
        return render_template('matrix.html', operations='transpose', matip=str(matrixA), matop=str(matrixB))
        # return self.home(str(operation), 'Transpose', str(row), str(col), str(matrixA),
        #                  str(transpose(matrixA, row, col)))
    elif (operation == 1):
        matrixB = upperDiagonal(matrixA, row, col)
        return render_template('matrix.html', operations='Upper Diagonal', matip=str(matrixA), matop=str(matrixB))
    elif (operation == 2):
        matrixB = lowerDiagonal(matrixA, row, col)
        return render_template('matrix.html', operations='Lower Diagonal', matip=str(matrixA), matop=str(matrixB))

@app.route('/exe', methods=['POST'])
def home():
    # print('at start')
    #mes = "hello"
    mes = request.form.get("word")
    # return jsonify(data=mes), 200
    res = edfuncntion(mes)
    encryted,decrypted = res
    # return ("Plain text :\t" +mes+"\nEncryted :\t"+encryted+"\n"+"Decrypted :\t"+decrypted)
    return render_template('RSA.html', tex = mes, enc = encryted, dec = decrypted)

@app.route('/hashMD', methods=['POST'])
def hashing():

    message = request.form.get('message')
    hashvalue = md5(message.encode("utf-8")).hex()
    # return home(message,md5(message.encode("utf-8")).hex()), 200
    return render_template("MDhash.html", sentence = message,output = hashvalue)

@app.route('/barcode',methods = ['POST'])
def generateBarcode():
    param_msg = str(request.form['message'])
    print(param_msg)
    barCode = EAN13(param_msg, writer=ImageWriter())
    barCode.save("Images/BarCode")
    res=[]
    with open("./BarCode.png", "rb") as image:
        encoded_string = base64.b64encode(image.read())
        res.append(encoded_string.decode("utf-8"))
    full_filename = os.path.join('BarCode.png')
    print(full_filename)
    return render_template("barcode.html", sentence=param_msg, output="Barcode has been generated successfully", image=full_filename)

@app.route('/qrcode',methods = ['POST'])
def generateQrcode():
    param_msg = request.form['message']
    url = pyqrcode.create(param_msg)
    url.png("Images/QrCode.png", scale = 8)
    res=[]
    # with open("./QrCode.png", "rb") as image:
    #     encoded_string = base64.b64encode(image.read())
    #     res.append(encoded_string.decode("utf-8"))

    return render_template("qrcode.html", sentence=param_msg, output="QR Code has been generated successfully")

@app.route('/captcha',methods = ['POST'])
def generateCaptcha():
    param_msg = request.form['message']
    img = Image.new('RGB', (200, 100), color = (255, 255, 255))
    fnt = ImageFont.truetype('./gillsans.ttf', 32)
    d = ImageDraw.Draw(img)
    R, G, B = random.randint(10,245), random.randint(10,245), random.randint(10,245),
    cmin = random.randint(50, 70)
    cmax = random.randint(90,120)
    for _ in range(cmin,cmax):
        r = R + random.randint(-10,10)
        g = G + random.randint(-10,10)
        b = B + random.randint(-10,10)
        diam = random.randint(2,4)
        x, y = random.randint(0,150), random.randint(0,50)
        draw = PIL.ImageDraw.Draw(img)
        draw.ellipse([x,y,x+diam,y+diam], fill=(r,g,b))
    img.filter(ImageFilter.BoxBlur(10))
    x=10
    y=10
    for i in range(len(param_msg)):
        d.text((x+(i*17),y),param_msg[i], font=fnt, fill=(0, 0, 0))
        if(random.randint(0, 4)%2==0):
            y=y+(random.randint(0,4) *2)
        else:
            y=y-(random.randint(0,4) *2)
    img.rotate(random.randint(-10,10))
    img.save('Images/captcha.png')
    res=[]
    # with open("./captcha.png", "rb") as image:
    #     encoded_string = base64.b64encode(image.read())
    #     res.append(encoded_string.decode("utf-8"))

    return render_template("captcha.html", sentence=param_msg, output="Captcha Code has been generated successfully", Image=res)


# app ruuning port
app.run(host='127.0.0.1', port=5011)