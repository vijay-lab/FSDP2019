# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:40:25 2019

@author: TAPAN


Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
temp = dataset.values
features = dataset.iloc[:, :1].values
labels = dataset.iloc[:, 1:].values
lab_bah=dataset.iloc[:, 1].values
lab_dan=dataset.iloc[:, 2].values

day=np.array(10)

day=day.reshape(1,1)
#model for bahubali
regressor_bah = LinearRegression()
regressor_bah.fit(features, lab_bah)

regressor_bah.predict(day)

#model for Dangal
regressor_dan = LinearRegression()
regressor_dan.fit(features, lab_dan)

regressor_dan.predict(day)

# BOth labels together
regressor = LinearRegression()
regressor.fit(features, labels)

regressor.predict(day)

print ("The Profit on day 10 of {} is {} and {} is {}".format('bahubali 2',regressor.predict(day)[0][0],'dangal' ,regressor.predict(day)[0][1]))