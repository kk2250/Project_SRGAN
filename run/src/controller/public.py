#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for
# from model import model

# UPLOAD_FOLDER = '/Users/kkim2250/Desktop/Project_SRGAN/'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

controller = Blueprint('public',__name__)
# controller.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        img_file = request.file['image']
        if img_file:
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join("image1.png"))
            return render_template('printpage.html', message=message)




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