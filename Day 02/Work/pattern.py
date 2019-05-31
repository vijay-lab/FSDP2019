# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:12:29 2019

@author: TAPAN


Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""


# Enter Number to print pattern
num = int(input("Enter Number to print Pattern: "))
# loop for incermentd * .
star_val=1
while (num>star_val):
    print("*" * star_val)
    star_val=star_val+1


# loop for decremented * .

for val in range(star_val):
    if (num>=val):
        print("*" * star_val)
        star_val=star_val-1
