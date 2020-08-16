import functools
from flask import Blueprint, request, render_template, redirect, flash, make_response
from scavengers_adventure.encrypto import decrypt

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('pulse.html')

@bp.route('/decrypt', methods=["GET", "POST"])
def decryption():
	if request.method == "POST":
		if 'file-input' not in request.files:
			return redirect('/decrypt')


		f = request.files['file-input']
		print(f)
		if f.filename == '':
			flash("No file input")
			return redirect('/decrypt')
		
		print(request.form['secret-key'])
		try:
			decrypted = decrypt(f.read(), request.form['secret-key'])
		except Exception as e:
			print(e)
			flash("Your key isn't completely accurate hmm..")
			return redirect('/decrypt')


		response = make_response(decrypted)
		response.headers.set('Content-Description', 'File Transfer')
		response.headers.set('Content-Type', 'multipart/image')
		response.headers.set('Content-Disposition', 'attachment', filename=f.filename)
		response.headers.set('Content-Length', len(decrypted))
		response.headers.set('Content-Transfer-Encoding', 'binary') 

		return response
	else:
		return render_template('submit.html')


@bp.route('/empty/wouldyouopenthisdoor')
def thedoor():
	return render_template('door.html')

@bp.route('/minds/canyoucatchthis')
def theeye():
	return render_template('eye.html')

@bp.route('/dark/findmeplease')
def theflashlight():
	return render_template('flashlight.html')

@bp.route('/direction/themcirclestho')
def tunnel():
	return render_template('Tunnel.html')


	
