"""
Code Challenge
  Name: 
    Resolution of an Image
  Filename: 
    resolution.py
  Problem Statement:
    Find the resolution of any jpeg Image file ( width x height )
  Hint:
    https://www.programiz.com/python-programming/examples/resolution-image
"""

def jpeg_res(filename):
   """"This function prints the resolution of the jpeg image file passed into it"""

   # open image for reading in binary mode
   with open(filename,'rb') as img_file:

       # height of image (in 2 bytes) is at 164th position
       img_file.seek(163)

       # read the 2 bytes
       a = img_file.read(2)
       
       a_0 = int('.'.join(str(ord(c)) for c in a[0]))
       a_1 = int('.'.join(str(ord(c)) for c in a[1]))
       
       # calculate height
       height = (a_0 << 8) + a_1

       # next 2 bytes is width
       a = img_file.read(2)

       a_0 = int('.'.join(str(ord(c)) for c in a[0]))
       a_1 = int('.'.join(str(ord(c)) for c in a[1]))
       

       # calculate width
       width = (a_0 << 8) + a_1

   print("The resolution of the image is",width,"x",height)

jpeg_res("img.jpg")
