# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:08:04 2019

@author: TAPAN
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Importing the dataset
uni_data = pd.read_csv('University_data.csv')
temp = uni_data.values
features = uni_data.iloc[:, 0:-1].values
labels = uni_data.iloc[:, -1].values

#Check if any NaN values in dataset
uni_data.isnull().any(axis=0)

#check data types for each column
print (uni_data.dtypes)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]




# Fitting Multiple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(features, labels)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)
features_test=[0,1,0,321,3,4,8.0,1]
features_test=np.array(features_test)
features_test=features_test.reshape(1,8)
# Predicting the Test set results
Pred = regressor.predict(features_test)