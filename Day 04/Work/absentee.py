# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:27:55 2019

@author: TAPAN
"""

new_list=[]

while True:
    
    input_name=input("Enter students name one by one\n\n>>")
    
    if not input_name:
        break
    
    
    
fp=open('absentee.txt','wt')


for value in input_name:
    
    
    fp.write(value)

fp.close()
    

