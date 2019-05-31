# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:30:41 2019

@author: TAPAN

Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""
string=input("Enter string to teranslate\n")

def translate_func(string):
    
    cons='bcdfghjklmnpqrstvwxyz'
    tl_list=[]
    
    for ch in string:
        if ch in cons:
            tl_list.append(ch+'o'+ch)
    
        else:
            tl_list.append(ch)
    tl_list = "".join( tl_list)
        
    return tl_list
    
    
print(translate_func(string))
    