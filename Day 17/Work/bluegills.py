# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:47:31 2019

@author: TAPAN

Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.

"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm



fs_df = pd.read_csv('bluegills.csv')
features = fs_df.iloc[:, 0:1].values
labels = fs_df.iloc[:, 1:].values


from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)

x=np.array(5)
x=x.reshape(1,-1)


print ("Predicting result with Linear Regression")
print ("Length of a 5 yr. old fish is",lin_reg_1.predict(x)[0][0])

# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()


##Polynomial
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features_poly, labels)



print ("Predicting result with Polynomial Regression")

print ("Length of a 5 yr. old fish in polynomial regressor is",lin_reg.predict(poly_object.transform(x))[0][0])

# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()


##Sorted
sfs_df=fs_df.sort_values(['age','length'])

features = sfs_df.iloc[:, 0:1].values
labels = sfs_df.iloc[:, 1:].values

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)




print ("Predicting result with Linear Regression")
print (lin_reg_1.predict(x))

# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()


##Polynomial
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features_poly, labels)



print ("Predicting result with Polynomial Regression")

print (lin_reg.predict(poly_object.transform(x)))

## predicting values
pred=lin_reg.predict(poly_object.fit_transform(features))

# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features,pred , color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()
