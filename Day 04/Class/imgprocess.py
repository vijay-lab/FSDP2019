"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Write a program that, given an image file will perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""


from PIL import Image
img = Image.open('data/sample.jpg').convert('LA')
img.save('data/greyscale.png')
img.show()


img_rotate = img.rotate(90)
img_rotate.show()

width, height = img_rotate.size
hw = width/2
hh = height/2

img_rotate = img_rotate.crop((hw-80,hh-102,hw+80,hh+102))
img.show()

img_rotate.thumbnail((75,75))
img_rotate.show()