"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    Take 9 space separated numbers from user. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
"""

import numpy as np

user_input = input("Enter 9 space separated numbers: ").split(" ")

# Creating Numpy Array
numpy_array = np.array( user_input, int )

# Changing numpy_array shape to 3X3 matrix
print ( np.reshape( numpy_array, (3,3) ) )
