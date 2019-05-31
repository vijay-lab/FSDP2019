# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:12:33 2019

@author: TAPAN

Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

import pandas as pd
import numpy as np

auto_df = pd.read_csv("Automobile.csv")



#
#nan_val_df=auto_df[auto_df['price'].isnull()]

#
#nan_val_df['price']=(nan_val_df['price']).fillna (round(auto_df['price'].mean(),0))
auto_df['price']=auto_df['price'].fillna(int(auto_df['price'].mean()))





# Get the values from Price column into a numpy.ndarray
np.array(auto_df['price'])

# Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
auto_df['price'].min()
auto_df['price'].max()
auto_df['price'].std()