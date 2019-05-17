# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:44:53 2019

@author: TAPAN
"""

from PIL import Image

img_name=input("Enter the image name\n") + '.jpg'

img = Image.open(img_name)



while True:
    
    choice=input("Enter your choice\n1.Grayscale\n2.Rotate 90\n3.crop\n4.thumbnail\n")
    
    if  not choice  :
        
        break
    
    
    elif (choice=='1'):
    
    
    
        img_gray=img.convert('L')
        
        img_gray.save('Gray_image.jpg')
        print("Your grayscale image is Gray_image.jpg")
    
    
    
    
    elif (choice=='2'):
    
    
        img_rotate=img.transpose(Image.ROTATE_90)
        
        img_rotate.save('rotated_image.jpg')
        
        print("Your rotated image is rotated_image.jpg")
    
    
    elif (choice=='3'):
    
    
    
        (img.crop(box=(0,0,160,204))).save('Cropped_image.jpg')
        
        #img_crop.save('Cropped_image.jpg')
        
        print("Your cropped image is crop_image.jpg")
        
        
        
    elif (choice=='4'):
        
        img.thumbnail((75, 75))
        img.save('image_thumbnail.jpg')
        
        print(img.size)
    
#        thumbnail=img.thumbnail((75, 75))
#        
#        
#        
#        thumbnail.save('Thumbnail.jpg')
#        
#        print("Your thumbnail is Thumbnail.jpg")