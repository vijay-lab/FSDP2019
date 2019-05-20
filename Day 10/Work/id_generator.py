# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:13:18 2019

@author: TAPAN
"""

#name=input("Enter Student Name\n")
#student_id=input("Enter Student ID\n")
#Course=input("Enter course Name\n")
#dob=input("Enter date of birth\n")
#valid_till=input("Enter valid till date\n")



from PIL import Image,ImageFont,ImageDraw


id_template=Image.open("id.png")




draw = ImageDraw.Draw(id_template)

logo = Image.open("logo.png")
logo_crop=(logo.crop(box=(0,0,580,650))).save('Cropped_image.png')

arial_font_name = ImageFont.truetype('arial.ttf', size=40)
arial_font = ImageFont.truetype('arial.ttf', size=30)

draw.text((50, 400), 'Tapan Vijay', fill='black', font=arial_font_name)




draw.text((500, 300), 'Student ID', fill='gray', font=arial_font_name)


draw.text((50, 500), 'ML & AI', fill='black', font=arial_font_name)
draw.text((500, 400), 'Date of Birth', fill='gray', font=arial_font)
draw.text((500, 500), 'Valid Till', fill='gray', font=arial_font)


id_template.paste(logo_crop, box=(0,0,50,100))



id_template.save("id_card.jpg", "JPEG")
