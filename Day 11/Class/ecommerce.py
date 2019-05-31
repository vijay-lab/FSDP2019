"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    in a random sample from a population) to it to see their effect.
    
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 1000)
print (incomes)

plt.title("Before adding outliers")
plt.hist(incomes, bins=50)
plt.show()

mean_value = np.mean(incomes)

median_value = np.median(incomes)


# After adding [100000,200000,300000,400000] outliers
outliers_list = np.random.randint(295,310,50)
incomes_outliers = np.append(incomes,outliers_list)

plt.title("After adding outliers")
plt.hist(incomes_outliers, bins=50)
plt.show()

mean_value_after_outliers = np.mean(incomes_outliers)

median_value_after_outliers = np.median(incomes_outliers)


print("Mean before adding outliers in incomes :"+str(round(mean_value,2)))
print("Median before adding outliers in incomes :"+str(round(median_value,2)))

print("Mean after adding outliers in incomes :"+str(round(mean_value_after_outliers,2)))
print("Median after adding outliers in incomes :"+str(round(median_value_after_outliers,2)))
