# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:35:30 2019

@author: TAPAN


Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm



iq_df = pd.read_csv('iq_size.csv')
features = iq_df.iloc[:, 1:].values
labels = iq_df.iloc[:, 0].values

features = sm.add_constant(features)

kept_features=features[:,[0,1,2,3]]

regressor_OLS=sm.OLS(exog=kept_features,endog=labels).fit()
regressor_OLS.summary()


kept_features=features[:,[0,1,2]]
regressor_OLS=sm.OLS(exog=kept_features,endog=labels).fit()
regressor_OLS.summary()

kept_features=features[:,[1,2]]
regressor_OLS=sm.OLS(exog=kept_features,endog=labels).fit()
regressor_OLS.summary()

kept_features=features[:,[1]]
regressor_OLS=sm.OLS(exog=kept_features,endog=labels).fit()
regressor_OLS.summary()

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(kept_features, labels)    

#while True:
#    regressor_OLS=sm.OLS(exog=kept_features,endog=labels).fit()
#    pvalues = regressor_OLS.pvalues
#    if pvalues.max() <= 0.05:
#        break
#    index = pvalues.argmax()
#    indices = pvalues.range(index)
#    kept_features = kept_features[:, ]

print("Only Brain  SIze mattter")

### total training
from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(features, labels)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor1.intercept_)  
print (regressor1.coef_)

x=[1,90,70,150]
x=np.array(x).reshape(1,4)
# Predicting the Test set results
Pred = regressor1.predict(x)

regressor1.score(features,labels)

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree =5)
features_poly = poly_object.fit_transform(features)


Poly_reg = LinearRegression()

Poly_reg.fit(features_poly, labels)

Poly_reg.score(features_poly,labels)
