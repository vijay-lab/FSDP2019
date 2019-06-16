# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:21:10 2019

@author: TAPAN

Q2. Code Challenge
code challenge - election data

1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the top parties vote % in each constituency for Rajasthan.

3. Visualize the total seats gained by each party in each states.

4. Visualize the total seats won by the parties in the whole country

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ele_df=pd.read_csv('election.csv')

#checkinh for missing data
ele_df.isnull().values.any()
raj=ele_df[ele_df['State'] =='Rajasthan']

plt.pie()