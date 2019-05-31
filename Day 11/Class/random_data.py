"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.

"""

import numpy as np
from collections import Counter

array_of_random_integers = np.random.randint( 5, 15, 40 )

frequency_counter = Counter( array_of_random_integers )

# Getting the most frequent value from the list of tuples of all the values
most_frequent_value = frequency_counter.most_common()[0][0]

print ( "The most Frequent Number is",most_frequent_value )


################## Another Way ##################

most_frequent_value = np.bincount( array_of_random_integers ).argmax()

print ( "The most Frequent Number is", most_frequent_value )
