#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for,send_file
from werkzeug import secure_filename
import os
import time
import cv2
import uuid
from src.model.test import img_run


controller = Blueprint('public',__name__)

@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        if request.files['image']:
            img_file = request.files['image']
            filename = secure_filename(img_file.filename)
            new_name = uuid.uuid4().hex.upper()[0:10]
            session['name'] = new_name
            with open('run/src/folder.txt','w+') as f:
                f.write(new_name)
            os.mkdir('run/src/static/images/{}'.format(new_name))
            img_file.save("run/src/static/images/{}/image.png".format(new_name))
            '/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/images/{}/image1.png'.format(new_name)
            img_run()
            return render_template('printpage.html', new_name=new_name)

@controller.route('/download')
def download():
    return send_file('/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/images/{}/image1.png'.format(session['name']), as_attachment=True, attachment_filename="image1.png")