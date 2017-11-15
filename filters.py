



from datetime import datetime
from flask import Flask, render_template
import random

app = Flask(__name__)


odds = range(1,60,2)

value1 = 0
value2 = 0
value3 = 0


photoId = 0
title = ""
author = ""


@app.route('/')
def index():

    global value1
    value1 = random.randint(1,10)
    global value2
    value2 = random.randint(1,10)
    global value3
    value3 = random.randint(1,10)

    print("its done")
    return render_template("index.html", v1 = value1, v2 = value2, v3 = value3)



@app.route('/newpage1')
def template_func():

    photoId = value1
    index = value1 - 1
    title = image_info[index]["title"]
    author = image_info[index]["flickr_user"]
    return render_template("newpage1.html", a1 = photoId, a2 = title, a3 = author)




@app.route('/newpage2')
def template_func1():

    photoId = value2
    index = value2 - 1
    title = image_info[index]["title"]
    author = image_info[index]["flickr_user"]
    return render_template("newpage2.html", a1 = photoId, a2 = title, a3 = author)


@app.route('/newpage3')
def template_func3():

    photoId = value3
    index = value3 - 1
    title = image_info[index]["title"]
    author = image_info[index]["flickr_user"]
    return render_template("newpage3.html", a1 = photoId, a2 = title, a3 = author)
