import flask
from flask import request, render_template, url_for
from flask_cors import CORS

from functions import *

app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    # return '''<h1>API homepage</h1>
    # <p>API for all operations.</p>'''
    return render_template("index.html")

@app.route('/huf', methods=['POST'])
def logs():
    return render_template("huffman.html")

@app.route('/rnlc', methods=['POST'])
def rnls():
    return render_template("runlength.html")
@app.route('/lzwhtml', methods=['POST'])
def rlzw():
    return render_template("lzw.html")
@app.route('/losslesstml', methods=['POST'])
def lossles():
    return render_template("lossless.html")


@app.route('/hufman', methods=['POST'])
def find_compression():
    print('at start')
    select = request.form.get("sentence")
    encd,decd,huffmanCode = buildHuffmanTree(select)
    return render_template("huffman.html",etdstring=select,hufcode=huffmanCode, encd=encd, decd=decd)

@app.route('/runlen', methods=['POST'])
def find_runlength():
    print('at start')
    select = request.form.get("sentence")
    RunlengthCode = printRLE(select)
    return render_template("runlength.html",etdstring=select,RunlengthCode=RunlengthCode)

@app.route('/lzw', methods=['POST'])
def find_lwz():
    print('at start')
    select = request.form.get("sentence")
    # encd,decd,lzw = buildHuffmanTree(select)
    word = lzw(select)
    compressed = compress(select)
    decompressed = decompress(compressed)
    return render_template("lzw.html",etdstring=select,lzwcode=word, compressed=compressed, decompressed=decompressed)

@app.route('/lossles', methods=['POST'])
def find_losscompression():
    print('at start')
    select = request.form.get("sentence")
    encd,decd,huffmanCode = buildHuffmanTree(select)
    return render_template("lossless.html",etdstring=select, encd=encd, decd=decd)
    # RunlengthCode = printRLE(select)
    # return render_template("lossless.html.html", etdstring=select, RunlengthCode=RunlengthCode)


app.run(host='127.0.0.1', port=5013)