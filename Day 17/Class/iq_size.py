"""
Are a person's brain size and body size (Height and weight) predictive of his
or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

What is the IQ of an individual with a given brain size of 90, 
height of 70 inches, and weight 150 pounds ? 
Build an optimal model and conclude which is more useful in predicting 
intelligence,Height, Weight or brain size.

file name "iq_size.py"

"""

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('iq_size.csv')
X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_train)
print (y_pred)


# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((38, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
#print (regressor_OLS.summary())

X_opt = X[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
#print (regressor_OLS.summary())

X_opt = X[:, [1, 2]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
#print (regressor_OLS.summary())

X_opt = X[:, [1]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
#print (regressor_OLS.summary())
print ("\n")
print ("Output : Brain Size is the only factor which is more useful in predicting intelligence.")