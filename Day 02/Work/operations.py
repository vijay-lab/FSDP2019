# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:19:24 2019

@author: TAPAN


Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
input_lst=int(input("Enter ints in ssv\n")).split(",")
def add_func():
    tot=0
    for val in input_lst:
        tot=tot+val
    return tot

def mult_func():
    tot=1
    for value in input_lst:
        tot=tot*value
    return tot

def lagrest_func():
    


    
    