# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:49:30 2019

@author: TAPAN
"""
my_dict = dict()

def fix_teen(age):
    if age >= 13 and age<=19:
        
        if age ==15 or age ==16:
            return 0
    return age
    
        

while True:
   
     
    name = input("Enter the name: ")
    if not name:
         break
    age = int(input("Enter the age: "))
    my_dict[name] = age
    
    
for k,v in my_dict.items():
    my_dict[k]=fix_teen(v)
    
print(sum(my_dict.values()))
    
