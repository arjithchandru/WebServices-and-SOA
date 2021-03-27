import flask
from flask import request, render_template, url_for
from flask_cors import CORS

from q2 import *

app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Q2', methods=['POST'])
def q2():
    mail = main_fun()
    return render_template("index.html", etdstring=mail)


app.run(host='127.0.0.1', port = 5014)