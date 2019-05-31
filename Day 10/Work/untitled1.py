# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:13:23 2019

@author: TAPAN





Code Challenge 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""

from PIL import Image, ImageDraw, ImageFont


img_cert = Image.open("Certi_temp.jpg").convert("RGBA")
logo = Image.open("logo1.png")

part_name=(input("Enter participants name\n")).upper()
#
#width = 50
#height = 40
# use one of these filter options to resize the image)     
#ANTIALIAS = logo.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter

logo_open = Image.open("logo.jpg")
stamp_open = Image.open("stamp.jpg")
sign_open = Image.open("sign.jpg")

img_cert.paste(sign_open, (50, 400))
img_cert.paste(stamp_open, (600, 350))
img_cert.paste(logo, (3, 50),logo)
img_cert.save("temp_w_logo.png")


certificate = Image.open("temp_w_logo.png")
draw = ImageDraw.Draw(certificate)

cop = ImageFont.truetype('Certificate.ttf', size=50)
arial = ImageFont.truetype('arial.ttf', size=50)
arial1 = ImageFont.truetype('arial.ttf', size=30)


# draw the message on the background

color = 'rgb(20, 20, 255)' # white color
draw.text((130, 50), 'Certification of Participation', fill=color, font=cop)

draw.text((175, 120), "This certifies that ", fill='gray', font=arial)


draw.text((135, 200), part_name , fill='black', font=arial)

draw.text((50, 280), "has actively participated in Forsk Summer Bootcamp ", fill=(51,51,255), font=arial1)

draw.text((50, 320), "for 2 Months and achieved grade A certification ", fill=(51,51,255), font=arial1)



certificate.save("new.png", "PNG")


