# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:59:05 2019

@author: TAPAN
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""



import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(150, 20, 1000)
print("Mean value is: ", np.mean(data))
print("Median value is: ", np.median(data))
plt.hist(data,100)
print("Varience is",np.var(data))
print("Standard Deviation is",np.std(data))


