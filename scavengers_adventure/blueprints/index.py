import functools
from flask import Blueprint, request, render_template, redirect, flash, make_response
from scavengers_adventure.encrypto import decrypt

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/decrypt', methods=["POST"])
def decryption():
	if 'file-input' not in request.files:
		return 'pffffffft'

	f = request.files['file-input']
	if f.filename == '':
		flash("No file input")
		return redirect('/')
	

	try:
		decrypted = decrypt(f.read(), request.form['secret-key'])
	except:
		flash("Your key isn't completely accurate hmm..")
		return redirect('/')


	response = make_response(decrypted)
	response.headers.set('Content-Description', 'File Transfer')
	response.headers.set('Content-Type', 'multipart/image')
	response.headers.set('Content-Disposition', 'attachment', filename=f.filename)
	response.headers.set('Content-Length', len(decrypted))
	response.headers.set('Content-Transfer-Encoding', 'binary') 

	return response
