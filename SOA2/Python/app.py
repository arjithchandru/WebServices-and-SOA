import flask
from flask import request, render_template, url_for
from flask_cors import CORS
from flask import request
import numpy as np

from Ecals import *
from Staticcals import *

app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    # return '''<h1>API homepage</h1>
    # <p>API for all operations.</p>'''
    return render_template("index.html")

@app.route('/log', methods=['POST'])
def logs():
    return render_template("logarithm.html")

@app.route('/GLC', methods=['POST'])
def glcs():
    return render_template("GLC.html")

@app.route('/stdv', methods=['POST'])
def stdvs():
    return render_template("std.html")

@app.route('/trig', methods=['POST'])
def trigs():
    return render_template("Trigonomentry.html")

@app.route('/rootes', methods=['POST'])
def rootess():
    return render_template("roots.html")

@app.route('/electronics', methods=['POST'])
def electronicss():
    return render_template("electronic.html")

@app.route('/linearreg', methods=['POST'])
def lers():
    return render_template("linearregression.html")



@app.route('/PVR', methods=['POST'])
# @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def find_missing():
    print('at start')
    select = request.form.get("tofind")
    if select == 'watts':
        I = float(request.form.get("ampere"))
        V = float(request.form.get("volts"))
        P = cal_watts(I, V)
        kW = cal_kiloWatt(P)
        SkVA = cal_kiloVoltamps(I, V)
        # return ("The Ampere: " + str(I) + " The watts :" + str(P) + " The Volts: " + str(V))
        result = ("The Ampere: " + str(I) + "The Volts: " + str(V) + "The watts :" + str(P) + " KiloWatt(kW): " + str(kW) + " KiloVoltAmps(kVA): " + str(SkVA))
    elif select == 'ampere':
        P = float(request.form.get("watts"))
        V = float(request.form.get("volts"))
        I = cal_amperes(P, V)
        kW = cal_kiloWatt(P)
        SkVA = cal_kiloVoltamps(I, V)
        # return ("The Ampere: " + str(I) + " The watts :" + str(P) + " The Volts: " + str(V))
        result = ("The Ampere: " + str(I) + "The Volts: " + str(V) + "The watts :" + str(P) + " KiloWatt(kW): " + str(kW) + " KiloVoltAmps(kVA): " + str(SkVA))
    elif select == 'volts':
        P = float(request.form.get("watts"))
        I = float(request.form.get("ampere"))
        V = cal_volts(P, I)
        kW = cal_kiloWatt(P)
        SkVA = cal_kiloVoltamps(I, V)
        # return ("The Ampere: " + str(I) + " The watts :" + str(P) + " The Volts: " + str(V))
        result = ("The Ampere: " + str(I) + "The Volts: " + str(V) + "The watts :" + str(P) + " KiloWatt(kW): " + str(kW) + " KiloVoltAmps(kVA): " + str(SkVA))
    else:
        result = select
    return render_template('electronic.html', message=result)

@app.route('/coverstion', methods=['POST'])
def convertion_api():
    print('at start')

    select = request.form.get("tofind")
    phase = request.form.get("tophase")
    if phase == 'single':
        Op = 'single'
        if select == 'VA':
            I = float(request.form.get("amps"))
            V = float(request.form.get("volt"))
            VA = cal_vaone(I, V)
            # print ("The Ampere: " + str(I) + " The watts :" + str(P) + " The Volts: " + str(V))
            result = ("The VA for single phase: "+ str(VA))


        elif select == 'Amps':
            VA = float(request.form.get("va"))
            V = float(request.form.get("volt"))
            amps = cal_vaampone(VA, V, Op)
            result = ("The Amps for single phase: " + str(amps))
            return render_template('electronic.html', coutput=result)
        elif select == 'kvaAmps':
            kVA = float(request.form.get("kva"))
            V = float(request.form.get("volt"))
            amps = cal_kvaampone(kVA, V, Op)
            result = ("The Ampere for single phase: " + str(amps))
            return render_template('electronic.html', coutput=result)
        elif select == 'Ampskva':
            I = float(request.form.get("amps"))
            V = float(request.form.get("volt"))
            kVA = cal_ampkvaone(I, V, Op)
            result = ("The kVA for single phase: " + str(kVA))
            return render_template('electronic.html', coutput=result)
    elif phase == 'three':
        Op = 'three'
        if select == 'VA':
            I = float(request.form.get("amps"))
            V = float(request.form.get("volt"))
            VA = cal_vathree(I, V)
            # print ("The Ampere: " + str(I) + " The watts :" + str(P) + " The Volts: " + str(V))
            result = ("The VA for Three phase: " + str(VA))
            return render_template('electronic.html', coutput=result)
        elif select == 'Amps':
            VA = float(request.form.get("va"))
            V = float(request.form.get("volt"))
            amps = cal_vaampone(VA, V, Op)
            result = ("The Amps for Three phase: " + str(amps))
            return render_template('electronic.html', coutput=result)
        elif select == 'kvaAmps':
            kVA = float(request.form.get("kva"))
            V = float(request.form.get("volt"))
            amps = cal_kvaampone(kVA, V, Op)
            result = ("The Ampere for three phase: " + str(amps))
            return render_template('electronic.html', coutput=result)
        elif select == 'Ampskva':
            I = float(request.form.get("amps"))
            V = float(request.form.get("volt"))
            kVA = cal_ampkvaone(I, V, Op)
            result = ("The kVA for Three phase: " + str(kVA))
            return render_template('electronic.html', coutput=result)
    elif phase == 'none':
        P = float(request.form.get("jwatts"))
        S = float(request.form.get("jsec"))
        J = cal_wjoule(P, S)
        result = ("The Watts :"+str(P)+" The Seconds :"+str(S)+" The Joule: " + str(J))
        return render_template('electronic.html', coutput=result)


@app.route('/staticcalc', methods=['POST'])
def staticcalc_api():
    print('static calc')
    String = request.form.get("lists")
    print(String)
    li = list(String.split(','))
    for i in range(0, len(li)):
        li[i] = int(li[i])
    # print(li)
    # li = [1,5,4,2,0]
    sd = standard_calculus(li)
    var = variance(li)
    return render_template('std.html',arrayentd=String, sd=sd, var=var)

@app.route('/mathlog2', methods=['POST'])
def mathlogic2_api():
    print("mathlogic api")
    select = request.form.get("mathlog2list")
    # print(select)
    if select == "gcdlist":
        nm = str(request.form.get("gcdlists"))
        # print(nm)
        nm = list(nm.split(','))
        for i in range(0, len(nm)):
            nm[i] = int(nm[i])
        # print(nm)
        # nm = [21, 3, 71]
        res = nm[0]
        # print(res)
        for i in range (len(nm)):
            res = gcd_function(res,nm[i])
            i = i+1
        gcd = res
        lcm = lcm_function(nm)
        return render_template('GLC.html',arrayented=nm, gcd=gcd, lcm =lcm)
    elif select == "sqlist":
        sqnumber = request.form.get("sqnum")
        # print(sqnumber)
        sqroot = find_sqroot(sqnumber)
        return render_template('index.html', sqroot=sqroot)
    elif select == "nsqlist":
        sqnumber = request.form.get("sqnum")
        rootsq = request.form.get("ntimes")
        # print(sqnumber)
        sqroot = find_sqroot(sqnumber)
        curoot = find_nsqroot(sqnumber, 3)
        nsqroot = find_nsqroot(sqnumber, rootsq)
        return render_template('roots.html',sqvalue=sqnumber, nthtime=rootsq, nsqroot=nsqroot, sqroot = sqroot, curoot = curoot)
    # elif select == "lcmlist":
    #     numbers = request.form.get("lcmnumber")
    #     print(numbers)
    #     arr = [2, 7, 3, 9, 4]
    #     lcmresult = lcm_function(arr)
    #     return render_template('index.html', lcmresult=lcmresult)
@app.route('/mathlog3', methods=['POST'])
def mathlogic3_api():
    print("trignomentry api")
    select = request.form.get("mathlog3list")
    if select == "alllist":
        theta = float(request.form.get("tdegree"))
        print(theta)
        sin = my_sin(theta)
        cos = my_cos(theta)
        tan = my_tan(theta)
        cosec = my_cosec(theta)
        sec = my_sec(theta)
        cot = my_cot(theta)
        if tan >= 1000 or (tan <= -10792.951559972442):
            tan = "-"
        if (cosec >= 1000) or (cosec <= -10792.951559972442):
            cosec = "-"
        if sec >= 1000 or (sec <= -10792.951559972442):
            sec = "-"
        if cos >= 1000 or (cos <= -10792.951559972442):
            cos = "-"
        if cot >= 1000 or (cot <= -10792.951559972442):
            cot = "-"

        return render_template('trigonomentry.html',degree=theta, sin=sin, cos=cos, tan=tan, cot=cot, sec=sec, cosec=cosec)
        # print(sin)

@app.route('/invmathlog3', methods=['POST'])
def invmathlogic3_api():
    select = request.form.get("opChoice")
    x = float(request.form.get("xaxis"))
    if select == "0":
        val = "arc sin"
        y = np.arcsin(x)
        y= y *(180/math.pi)
    if select == "1":
        val = "arc cos"
        y = np.arccos(x)
        y = y * (180 / math.pi)
    if select == "2":
        val = "arc tan"
        y = math.atan(x)
        y = y * (180 / math.pi)

    return render_template('trigonomentry.html', val=val, x=x, y=y)

@app.route('/mathlog1', methods=['POST'])
def logcalc():
    opChoice = int(request.form.get('opChoice'))

    if (opChoice == 0 and not request.form.get('num3') and not request.form.get('base')):
        output = 'Enter the required data'
        return render_template('logarithm.html', data=output)
    elif (opChoice == 1 and not request.form.get('num')):
        output = 'Enter the required data'
        return render_template('logarithm.html', data=output)
    elif (opChoice == 2 and not request.form.get('data') and not request.form.get('pow')):
        output = 'Enter the required data'
        return render_template('logarithm.html', data=output)

    vOpName = data = pow = num = num3 = 0

    if (opChoice == 0):
        data = int(request.form.get('numb'))
        base = int(request.form.get('base'))

        vOpName = "Log "
        vresult = log(data, base)
        output = "The number : " + str(data) + " The base : " + str(base) + " The function : " + str(vOpName) + " The result : " + str(vresult)
    elif (opChoice == 1):
        data = int(request.form.get('numn'))

        vresult = nLog(data)
        vOpName = "Natural Log "
        output = "The number : " + str(data) + " The function : " + str(vOpName) + " The result : " + str(vresult)

    elif (opChoice == 2):
        data = int(request.form.get('numa'))
        pow = int(request.form.get('pow'))
        vresult = antiLog(data, pow)
        vOpName = "AntiLog "
        output = "The number : " + str(data) + " The power : " + str(pow) + " The function : " + str(vOpName) + " The result : " + str(vresult)

    # print(pow)
    # print(data)
    # print(vresult)
    # print(vOpName)


        # return home(str(data), str(vresult), str(vOpName), str(pow), str(data), str(data))
    return render_template('logarithm.html', data=output)

@app.route('/linearregression', methods=['POST'])
def lerrs():
    param_xList = request.form['xList']
    param_yList = request.form['yList']

    param_xList = list(param_xList.split(','))
    for i in range(0, len(param_xList)):
        param_xList[i] = float(param_xList[i])

    param_yList = list(param_yList.split(','))
    for i in range(0, len(param_yList)):
        param_yList[i] = float(param_yList[i])

    if len(getNumberList(param_xList)) == len(getNumberList(param_yList)):
        print(1)
        xList = getNumberList(param_xList)
        yList = getNumberList(param_yList)
        sum_xlist = 0
        sum_ylist = 0
        sum_xSquare = 0
        sum_xy = 0
        n = len(xList)
        for i in range(n):
            sum_xlist = sum_xlist + xList[i]
            sum_ylist = sum_ylist + yList[i]
            sum_xSquare = sum_xSquare + (xList[i] * xList[i])
            sum_xy = sum_xy + (xList[i] * yList[i])

        slope = (n * sum_xy - sum_xlist * sum_ylist) / (n * sum_xSquare - sum_xlist * sum_xlist);
        intercept = (sum_ylist - slope * sum_xlist) / n
        equartion = "y = " + str(slope) + " x = " + str(intercept)
        res = [str(equartion)]

    else:
        res = "OOPS ! Some internal error"
    return render_template("linearregression.html", Xarrayented=param_xList, Yarrayented=param_yList, res=res)

app.run(host='127.0.0.1', port=5012)