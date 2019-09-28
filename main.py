import os
import sys
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import json
from shutil import copyfile
from models.FileManager import FileManager
from models.FtpManager import FtpManager
import smtplib
from libraries.ErrorNotification import ErrorNotification
from ftplib import FTP

app = Flask(__name__)
fileManager = FileManager()
FtpManager = FtpManager()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/file/copy', methods=['POST'])
def copyFile():

	try:
		success = True
		response = fileManager.manage_file(request.form['source'], request.form['destination'])
	except Exception as e:
		success = False
		response = e.args
	finally:
		return formatResponse(response, success)

@app.route('/file/move', methods=['POST'])
def moveFile():
	
	try:
		success = True
		response = fileManager.manage_file(request.form['source'], request.form['destination'], True)
	except Exception as e:
		success = False
		response = e.args
	finally:
		return formatResponse(response, success)

@app.route('/file/delete', methods=['POST', 'DELETE'])
def deleteFile():

	try:
		success = True
		response = fileManager.remove_file(request.form['source'])
	except Exception as e:
		success = False
		response = e.args
	finally:
		return formatResponse(response, success)

@app.route('/file/checksum', methods=['POST'])
def checksum():
	try:
		success = True
		response = fileManager.get_checksum(request.form['source'])
	except Exception as e:
		success = False
		response = e.args
	finally:
		return formatResponse(response, success)

@app.route('/file/serve2Ftp', methods=['GET'])
def serve2Ftp():
	try:
		return True
		success = True
		response = FtpManager.serve2Ftp('santa_monica.jpg')
		return formatResponse(response, success)
	except Exception as e:
		success = False
		return formatResponse(e.args, success)

def formatResponse(data, success = True):
	if not success:
		errorNotification = ErrorNotification()
		errorNotification.send_notification(request.url_rule)

	data = {
		'response' : str(data),
		'success' : success
	}
	return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')