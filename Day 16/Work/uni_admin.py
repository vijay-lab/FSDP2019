# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:47:55 2019

@author: TAPAN


Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

univ_df=pd.read_csv("University_data.csv")

features=univ_df.iloc[:,:-1].values
label=univ_df.iloc[:,-1 ].values

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])

features=onehotencoder.fit_transform(features).toarray()
# Dummy Trap removed
features = features[:, 1:]

from sklearn.model_selection import train_test_split
features_train, features_test, label_train, label_test = train_test_split(features, label, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train, label_train)
label_pred=regressor.predict(features_test)

#from sklearn.metrics import r2_score
#print(r2_score(label_test,label_pred))
#
#Score_trn = regressor.score(features_train, label_train)
#Score_tst = regressor.score(features_test, label_test)
#from sklearn import metrics  
#print('Mean Absolute Error:', metrics.mean_absolute_error(label_test, label_pred))  
#print('Mean Squared Error:', metrics.mean_squared_error(label_test, label_pred))  
#print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(label_test, label_pred)))  
#
#print (np.mean(label))


chance=np.array([0,0,0,1,0,350,3.7,4,8.89,0])
chance=chance.reshape(1,-1)

chance=onehotencoder.fit_transform(chance).toarray()

print("Chances of Admission Are:",regressor.predict(chance)[0], "%")

