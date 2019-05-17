# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:02:47 2019

@author: TAPAN
"""


        
        
        
user_input = input("Enter ssv :").split()

input_length  = len(user_input)
count = 0
pallindromic_integer = False

for num in user_input:
    if int(num) > 0:
        count += 1

if count == input_length:
    for positive_num in user_input:
        if positive_num == positive_num[::-1]:
            pallindromic_integer = True

print(pallindromic_integer)

user_input = input("Enter ssv :").split()
if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
    
    
    