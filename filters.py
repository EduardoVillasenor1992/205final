from datetime import datetime
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import random
UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

odds = range(1,60,2)

value1 = 0
value2 = 0
value3 = 0


photoId = 0
title = ""
author = ""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("newpage1.html")

    else:
        print("its done")
        return render_template("index.html")



@app.route('/newpage1')
def template_func():

    # photoId = value1
    # index = value1 - 1
    # title = image_info[index]["title"]
    # author = image_info[index]["flickr_user"]
    return render_template("newpage1.html")
