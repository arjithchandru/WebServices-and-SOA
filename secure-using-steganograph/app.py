from flask import Flask, render_template, redirect, url_for, request
from forms import encodeForm, decodeForm
import os
from PIL import Image
import secrets
from alg_apply import original_text, enc_alg, dec_alg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QWERTYU12345673ERFGHBNTRDGFCN6RUFKJV'

def save_image(im):
	_,ext = os.path.splitext(im.filename)
	fn = secrets.token_hex(4)+'_'+'org'+ext
	pic_path = os.path.join(app.root_path, "static/org_pic", fn)
	i = Image.open(im)
	i.save(pic_path)
	print('saved')
	# enc_alg(pic_path)
	# print('Return password: ', enc_alg(pic_path))
	return pic_path

@app.route('/encode', methods= ['GET','POST'])
def encode():
	title = '-encode'
	form = encodeForm()
	if form.is_submitted():
		print("submitted")
		# return redirect(url_for('encode'))
	if form.validate_on_submit():
		print('ok done!')
		pic = form.picture.data
		try:
			pwd, img = enc_alg(save_image(pic))
			pd_ret = str(pwd)
			im_ret = str(img).split('/')[-1]

			print('***************',str(img).split('/')[-1
				])
			return render_template('dl_page.html', pd_ret=pd_ret, im_ret=im_ret)
		except:
			return render_template('retrieve_msg.html', message='error')
			pass
	else:
		print('not done')
	return render_template('encode.html', title=title, form=form)

def save_deImage(org, enc):
	# print(org.filename, enc.filename)
	_,ext_o = os.path.splitext(org.filename)
	_,ext_e = os.path.splitext(enc.filename)
	sec = secrets.token_hex(4)
	fn_org = sec+'_'+'d'+'_'+'org'+ext_o
	fn_enc = sec+'_'+'d'+'_'+'enc'+ext_e
	pic_path_o = os.path.join(app.root_path, "static/de_org_pic", fn_org)
	pic_path_e = os.path.join(app.root_path, "static/de_enc_pic", fn_enc)
	im_o = Image.open(org).save(pic_path_o)
	im_e = Image.open(enc).save(pic_path_e)
	return pic_path_o, pic_path_e

@app.route('/decode', methods= ['GET','POST'])
def decode():
	title = '-decode'
	form = decodeForm()
	if form.is_submitted():
		print('decode form submitted')
	if form.validate_on_submit():
		print('decode form ok done!')
		org_pic = form.picture_o.data
		enc_pic = form.picture_e.data
		# save_deImage(org_pic, enc_pic)
		pic_path_o, pic_path_e = save_deImage(org_pic, enc_pic)
		message = str(dec_alg(pic_path_o, pic_path_e))
		return render_template('retrieve_msg.html', message = message)
	else:
		print('not done')

	return render_template('decode.html', title =title, form=form)

@app.route('/')
def home():
	return render_template('index.html')


if __name__ == '__main__':
	# app.run(debug = True)
	app.run()
