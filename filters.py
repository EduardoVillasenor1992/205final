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

title = [os.listdir("static/Uploads")]
print(title)
print(title[0][0])

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
            print(filename)
            return render_template("newpage1.html")

    else:
        print("its done")
        return render_template("index.html")



@app.route('/newpage1')
def template_func():

    return render_template("newpage1.html", titles = title)



################################################################################
# filters for image

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
