# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:02:08 2019

@author: TAPAN
"""
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



template = Image.new('RGB', (1280,720), (0, 13, 30))
template.save("template.png", "PNG")


img = Image.open("template.png")
draw = ImageDraw.Draw(img)

selectFont = ImageFont.truetype("ariel.ttf", size = 50)




draw.text( (250,70), "CERTIFICATE OF APPRICIATION", (43,107,189), font=selectFont)

img.save('sample_certi.png')


filename=Image.open('template.png')
ironman = Image.open(filename, 'r')


filename1=Image.open('logo.png')
bg = Image.open(filename1, 'r')
alpha=0.5
out = Image.blend(img,filename1,alpha)
out.show()
#
#out = filename * (1.0 - 1) + filename1 * 0.50



text_img = Image.new('RGB', (1280,720), (0, 13, 30))
text_img.paste(bg, (120,360))


text_img.paste(ironman, (0,0))
text_img.save("new_certi.png", format="png")
# (x,y) is the starting position for the draw object
# text is the text to be entered
# (r,g,b) represents the color eg (255,0,0) is Red
# font is used to specify the Font object