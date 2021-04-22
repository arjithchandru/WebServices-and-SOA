from forms import encodeForm, decodeForm
import cv2
import numpy as np
from PIL import Image
import os
import re
# print('treda: ',os.path.dirname(os.path.abspath(__file__)))
def original_text():
	form = encodeForm()
	txt = bin(int.from_bytes(form.text.data.encode(), 'big')).replace('b','')
	return txt
def enc_alg(im):
	a = []
	img = cv2.imread(im)
	new_name = im.split('\\')[-1].replace('org','enc')
	print(im,new_name)
	row,col,ch=img.shape
	flat_img=img.flatten()
	text = original_text()
	try:
		# print(text)
		for i in text:
			c=[int(i)]
			c.append(0)
			a.append(c)
		flat_txt=np.array(a).flatten()
		# print('password:',len(flat_txt))
		zeros=np.zeros((len(flat_img)-len(flat_txt),),dtype=int)
		encoded_txt=np.append(flat_txt,zeros)
		encoded_img_flat=np.subtract(flat_img,encoded_txt)
		encoded_img=np.reshape(encoded_img_flat,(row,col,ch))
		root = os.path.dirname(os.path.abspath(__file__))
		enc_path = new_name
		# print('++++++++++++++++'+enc_path)

		cv2.imwrite(enc_path, encoded_img)
		# cv2.imshow('image',img)
		# cv2.waitKey(0)
		return len(flat_txt),new_name
	except:
		pass

	# C:\Users\ASUS-PC\Desktop\sten_webapp\static\org_pic\12d57ad1_org.jpg

def dec_alg(o,e):
	decodedTxt=[]
	form = decodeForm()
	length = int(form.pwd_d.data)
	print(o,'--------------------',e,'--------------------',length)
	org_img = cv2.imread(o)
	flat_org_img = org_img.flatten()
	enc_img = cv2.imread(e)
	flat_enc_img = enc_img.flatten()

	try:
		sub = np.subtract(flat_org_img[:length], flat_enc_img[:length])
		for i in range(length):
			if i%2 == 0:
				decodedTxt.append(str(sub[i]))

		txt=''.join(decodedTxt)
		rev=txt[:1]+'b'+txt[1:]
		n = int(rev, 2)
		message = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
		return message
	except:
		return 'error'
	# cv2.imshow('im', org_pic)
	# cv2.imshow('iam', enc_pic)
	# cv2.waitKey(0)
	