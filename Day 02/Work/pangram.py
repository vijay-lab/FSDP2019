# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:44:30 2019

@author: TAPAN
"""

string = list(input("Enter any string to check::\n").lower())

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

tl=[]
val=0

for ch in string: 
 if ch not in tl: 
  tl.append(ch) 

len(tl)       
        
for elements in tl:
    if elements in alphabet:
        val += 1
if val == 26:
    print ("Pangram")
else:
    print ("Not Pangram")
