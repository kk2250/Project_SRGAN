#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for,send_file
from werkzeug import secure_filename
import os
import time
import cv2
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
            img_file.save("run/src/static/image.png")
            img_run()
            return render_template('printpage.html')

@controller.route('/download')
def download():
    return send_file('/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/image1.png', as_attachment=True, attachment_filename="image1.png")