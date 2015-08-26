from PIL import Image, ImageDraw

mohan = Image.open("Pictures/mohan.jpg")
bear = Image.open("Desktop/stoneteddybear.jpg")
butterfly = Image.open("Pictures/blue.jpg")
photo = Image.open("Pictures/photo.png")
aaron = Image.open("Pictures/aaron.jpg")
        
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

##def posterize(im, levels):
##
##    #Figure out thresholds for the pixel colors
##    increment = 255//levels
##    thresholds = range(1, 256, increment)
##
####    im = copy.copy(im)
####    img = im.load()
##    poster=Image.new("RGB", (im.size[0],im.size[1]))
##    draw = ImageDraw.Draw(poster)
##    #Iterate through the image
##    for y in range(im.size[1]):
##        for x in range(im.size[0]):
##
##            #Get a new RGB tuple based on thresholds
##            new = []
##            for c in range(3):
##                color = im[x, y][c]
##                level = bisect_left(thresholds, color)-1
##                new.append(thresholds[level])
##
##            #Put the new pixel on the image
##            poster[x, y] = tuple(new)
##
##    #Return the image
##    poster.show()
