# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:03:29 2019

@author: TAPAN
"""
import random as rn


fruits=['mango','apple','banana','pear','kiwi']


cp_list=[]

cp_list=list((rn.choice(fruits)))



print(cp_list)

input_list= list(input("Guess a fruit name::\n"))


for index, item in enumerate(input_list):
    
    for index, item in enumerate(cp_list):
        
        