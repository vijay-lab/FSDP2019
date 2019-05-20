# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:43:04 2019

@author: TAPAN


Watermarking Application

Have some pictures you want copyright protected? Add your own logo or text lightly 
across the background so that no one can simply steal your graphics off your site. 
Make a program that will add this watermark to the picture.


"""

from PIL import Image, ImageDraw, ImageFont

image = Image.open('sample.jpg')
width, height = image.size
 
draw = ImageDraw.Draw(image)
text = "Demo Watermark"
 
font = ImageFont.truetype('arial.ttf', 12)
textwidth, textheight = draw.textsize(text, font)
 
# calculate the x,y coordinates of the text
margin = 5
x = width - textwidth - margin
y = height - textheight - margin
 
# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
 
image.save('sampled_watermark.png')


#### transparent watermark
def watermark_with_transparency(input_image_path,output_image_path, watermark_image_path,position):
    
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
 
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)
 
 
img = input('Enter image name\n ')+'.jpg'
watermark_with_transparency(img, 'sample_watermarked3.jpg',
                                'image_thumbnail.png', position=(0,0))