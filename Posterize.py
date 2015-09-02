## Needs PIL, pygame, VideoCapture, time to run!!! Make sure all are installed"

from PIL import *
from pygame import *
from VideoCapture import *
import time

##bear = Image.open("Desktop/stoneteddybear.jpg")
##butterfly = Image.open("Pictures/blue.jpg")
##photo = Image.open("Pictures/photo.png")
##aaron = Image.open("Pictures/aaron.jpg")
        
def binarize(im, thresh):
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            (red,green,blue) = im.getpixel( (x,y) )
            if thresh <= (red *21/100) + (green *72/100) + (blue * 7/100):
                im.putpixel((x, y),(255,255,255))
            else:
                im.putpixel((x, y),(0,0,0))
    im.show()
def posterize(im):
    (width,height)=im.size
    poster=Image.new("RGB", (width,height))
    draw = ImageDraw.Draw(poster)
    for x in range(width):
        for y in range(height):
            (red,green,blue) = im.getpixel((x,y))
            newRed = red & 0xC0
            newGreen = green & 0xC0
            newBlue = blue & 0xC0
            poster.putpixel((x,y),(newRed,newGreen,newBlue))
    poster.show()
    poster.save("PosterTest2.jpg")

#def posterizePoint(im):

def takeIm():
    cam = Device()
    cam.saveSnapshot('image.jpg')

def imageCapture():
    print "Taking initial picture in 1 second"
    time.sleep(1)
    cam = Device()
    cam.saveSnapshot("initial.jpg")
    initial = Image.open("initial.jpg")
    (width, height) = initial.size
    print "Taking second picture in 10..."
    time.sleep(1)
    print "9..."
    time.sleep(1)
    print "8..."
    time.sleep(1)
    print "7..."
    time.sleep(1)
    print "6..."
    time.sleep(1)
    print "5..."
    time.sleep(1)
    print "4..."
    time.sleep(1)
    print "3..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "1..."
    time.sleep(1)
    print "Taking photo!"
    cam.saveSnapshot("new.jpg")
    new = Image.open("new.jpg")
    counter = 0
    for x in range(width):
        for y in range(height):
            (initialRed,initialGreen,initialBlue) = initial.getpixel((x,y))
            (newRed,newGreen,newBlue) = new.getpixel((x,y))
            if newRed <= initialRed-25 or newRed >= initialRed+25:
                if newGreen <= initialGreen-25 or newGreen >= initialGreen+25:
                    if newBlue <= initialBlue-25 or newBlue >= initialBlue+25:
                        counter = counter + 1
            else:
                pass
    if counter >= 300000:
        posterize(new)
        
    
##def initalFrame():
## 
##    

