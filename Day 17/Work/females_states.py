# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:49:45 2019

@author: TAPAN


Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm



fs_df = pd.read_csv('Female_Stats.csv')
features = fs_df.iloc[:, 1:].values
labels = fs_df.iloc[:, 0].values

#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)
features = sm.add_constant(features)
#adds a constant column to input data set.


features_opt = features[:, [0,1, 2]]

regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()



"""So we conclude that Both Predictors (Independent Variables) Are Significant For A Students’ Height"""
regressor_OLS.pvalues
print("Effect of mom's height",regressor_OLS.params[1])

print("Effect of dad's height",regressor_OLS.params[2])

