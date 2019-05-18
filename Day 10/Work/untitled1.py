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


img = Image.new('RGBA', (728,542), 'White')
img.save("Certi_Template.png", "PNG")

img_cert = Image.open("Certi_Template.png").convert("RGBA")
logo = Image.open("logo.png")
border= Image.open("border.png").convert("RGBA")

part_name=input("Enter participants name\n")

width = 50
height = 40
# use one of these filter options to resize the image)     
ANTIALIAS = logo.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
ANTIALIAS.save("ANTIALIAS.PNG")
ANTIALIAS = Image.open("ANTIALIAS.png")

img_cert.paste(ANTIALIAS, (250, 200),ANTIALIAS)

img_cert.paste(border, (0, 0),border)

img_cert.save("temp_w_logo.png")

certificate = Image.open("temp_w_logo.png")

draw = ImageDraw.Draw(certificate)

font = ImageFont.truetype('Certificate.ttf', size=90)
arial = ImageFont.truetype('arial.ttf', size=60)
arial1 = ImageFont.truetype('arial.ttf', size=40)


# draw the message on the background

color = 'rgb(20, 20, 255)' # white color
draw.text((30, 30), 'Certification of Participation', fill=color, font=font)

draw.text((30, 90), "Forsk Labs Awards ", fill='gray', font=arial)


draw.text((30, 150), part_name , fill='RED', font=arial)

draw.text((30, 260), "for Excellent performance at Summer Bootcamp ", fill='RED', font=arial1)




certificate.save("new.png", "PNG")


