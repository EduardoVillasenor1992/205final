



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
    return render_template("index.html")



@app.route('/newpage1')
def template_func():

    # photoId = value1
    # index = value1 - 1
    # title = image_info[index]["title"]
    # author = image_info[index]["flickr_user"]
    return render_template("newpage1.html")
