# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:13:46 2019

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
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

fish_data=pd.read_csv("bluegills.csv")
fish_data=fish_data.sort_values(['age','length'])
x=fish_data.iloc[:,0:1].to_numpy()
y=fish_data.iloc[:,1].to_numpy()

lin_regressor=LinearRegression()
lin_regressor.fit(x,y)

plt.scatter(x,y,color = 'green')
plt.plot(x,lin_regressor.predict(x))
plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

##Polynomial Regressor
## just transform the data into polynomial to use LR model
poly_obj=PolynomialFeatures(degree=4)
x_new = poly_obj.fit_transform(x)


#fitting of data

lin_reg_poly = LinearRegression()
lin_regressor.fit(x_new, y)

val=np.array(5)
val=val.reshape(1,-1)


# Visualising the Polynomial Regression results
pred=lin_regressor.predict(poly_obj.fit_transform(x))
plt.scatter(x, y, color = 'red')
plt.plot(x,pred , color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()
