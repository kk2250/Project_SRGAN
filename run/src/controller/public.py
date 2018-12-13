#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for,send_file
from werkzeug import secure_filename
import os
# from model import model

# UPLOAD_FOLDER = '/Users/kkim2250/Desktop/Project_SRGAN/'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

controller = Blueprint('public',__name__)
# controller.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# controller.config = {}

# @controller.record
# def record_params(setup_state):
#   app = setup_state.app
#   controller.config = dict([(key,value) for (key,value) in app.config.items()])

@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        if request.files['image']:
            img_file = request.files['image']
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join("run/src/static/image1.png"))
            # with open('run/src/static/image1.png') as f:
            return render_template('printpage.html')

@controller.route('/download')
def download():
    return send_file('/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/image1.png', as_attachment=True, attachment_filename="image1.png")


# @controller.route('/out',methods=['GET','POST'])
# def printpage():
#     if request.method == 'GET':
#         return render_template('homepage.html')
#     elif request.method == 'POST':
#         text_file = request.file['upload']
#         text = request.form['summ']
#         if text_file:
#             pass
#             # model.sum(text_file)
#         elif text:
#             pass
#             # model.sum(text)
#         return render_template('printpage.html', message=message)