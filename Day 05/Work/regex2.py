# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:04:09 2019

@author: TAPAN
"""

import re
list_of_eml=[]
list_of_eml2=[]

while True:
    
    email=input("enter an email address>>")
    
    
    if not email:
        break

    list_of_eml.append(email)


for email in list_of_eml:
    
    if re.match(r'^[A-Za-z0-9_-]+@[A-Z0-9a-z]+\.[a-z]{2,4}$', email):
        
        
  
        #list_of_eml.append(email)
        list_of_eml2.append(email)
      
print(sorted(list_of_eml2))