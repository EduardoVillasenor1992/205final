from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


im = Image.open("Tree.jpg") # Colling filter
im2 = Image.open("Clouds.jpg") # Negative filter
im3 = Image.open("Clouds.jpg") # Sepia filter
im4 = Image.open("Grass.jpg") # Gray filter
im5 = Image.open("Clouds.jpg") # Warm filter


@app.route('/')
def coolingFilter(cooling_filter):
    filter1 = []
    for i in cooling_filter.getdata():
        intensity = (10 + i[0], 50 + i[1], 255 + i[2])
        filter1.append(intensity)
    cooling_filter.putdata(filter1)
    cooling_filter.save("CoolingFilter.png")
    #return render_template('pics.html', filter1)
coolingFilter(im)


def negative(negative_filter):
    filter2 =[]
    for i in negative_filter.getdata():
        intensity = (255 - i[0], 255 - i[1], 255 - i[2])
        filter2.append(intensity)
    negative_filter.putdata(filter2)
    negative_filter.save("Negative.png")
negative(im2)


def sepia(sepia_filter):
    filter3 = []
    for i in sepia_filter.getdata():
        intensity = (130 + i[0], 66 + i[1], 20 + i[2])
        filter3.append(intensity)
    sepia_filter.putdata(filter3)
    sepia_filter.save("Sepia.png")
sepia(im3)


def gray(gray_filter):
    filter4 =[]
    for i in gray_filter.getdata():
        intensity = int ((i[0] +i[1] +i[2])/3)
        temp = (intensity,intensity,intensity)
        filter4.append(temp)
    gray_filter.putdata(filter4)
    gray_filter.save("Gray.png")
    
gray(im4)

def warm(warm_filter):
    filter5=[]
    for i in warm_filter.getdata():
        intensity = (150 + i[0], 177 + i[1], 19 + i[2])
        filter5.append(intensity)
    warm_filter.putdata(filter5)
    warm_filter.save("Warm.jpg")
warm(im5)    






    

    
    
