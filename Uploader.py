###################################
# Course: CST 205
# Title: Photo Uploader
# Authors: Ishtar Perez(filter basic layout, @routes(), github setup), Ben Lenz(file upload system, image displaying,), Edward Villasenor(HTML layout, script for filter display, general layout, github setup)
# Date: 12/09/2017
# GITHUB link: https://github.com/EduardoVillasenor1992/205final
# Description: Allows the user to upload an image file of their choice, and displays it in a block format. There are also seperate links between the homepage and gallery page to navigate
################################
from datetime import datetime
from PIL import Image
import glob
import os
import os.path
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import random
UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

image_list = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#checks file to see if it is an image extension, checking the formats with the list above ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET','POST'])
def index():
    ## if the upload button is pressed, get the filename, check if it is an imaage and then save it to the uploads folder, and add the name to the list of pictures to be displayed on the next page
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            title = [os.listdir("static/Uploads")]
            return render_template("Gallery.html", titles = title)

    else:
        return render_template("index.html")


#newpage1 = image gallery page, input is a list of the images in upload folder
@app.route('/newpage1')
def template_func():
    title = [os.listdir("static/Uploads")]
    return render_template("Gallery.html", titles = title)



################################################################################
# filters for image, they currently do not work,

def coolingFilter(cooling_filter):
    filter1 = []
    for i in cooling_filter.getdata():
        intensity = (10 + i[0], 50 + i[1], 255 + i[2])
        filter1.append(intensity)
    cooling_filter.putdata(filter1)
    cooling_filter.save("CoolingFilter.jpg")


def negative(negative_filter):
    filter2 =[]
    for i in negative_filter.getdata():
        intensity = (255 - i[0], 255 - i[1], 255 - i[2])
        filter2.append(intensity)
    negative_filter.putdata(filter2)
    negative_filter.save("Negative.jpg")



def sepia(sepia_filter):
    filter3 = []
    for i in sepia_filter.getdata():
        intensity = (130 + i[0], 66 + i[1], 20 + i[2])
        filter3.append(intensity)
    sepia_filter.putdata(filter3)
    sepia_filter.save("Sepia.jpg")



def gray(gray_filter):
    filter4 =[]
    for i in gray_filter.getdata():
        intensity = int ((i[0] +i[1] +i[2])/3)
        temp = (intensity,intensity,intensity)
        filter4.append(temp)
    gray_filter.putdata(filter4)
    gray_filter.save("Gray.jpg")



def warm(warm_filter):
    filter5=[]
    for i in warm_filter.getdata():
        intensity = (150 + i[0], 177 + i[1], 19 + i[2])
        filter5.append(intensity)
    warm_filter.putdata(filter5)
    warm_filter.save("Warm.jpg")
