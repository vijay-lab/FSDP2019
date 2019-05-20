# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:16:43 2019

@author: TAPAN

Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""


import numpy as np 

x = np.linspace(5, 15, 40, dtype=np.int64)
counts = np.bincount(x)
print (np.argmax(counts))


#by counter
from collections import Counter

b = Counter(x)
print (b.most_common(1))



