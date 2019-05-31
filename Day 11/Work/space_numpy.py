# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:02:53 2019

@author: TAPAN

Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np
list1=input("Enter 9 space separated numbers: ").split(" ")
ndarr1=np.array(list1,dtype= 'int64')#convering list to numpy array of integers
print(ndarr1)
matrix1=ndarr1.reshape(3,3)#reshaping array to matrix of (3,3)
print(matrix1)