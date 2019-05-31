"""
How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. 
The researchers (Cook and Weisberg, 1999) measured and recorded the following 
data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

How is the length of a bluegill fish best related to its age? 
(Linear/Quadratic nature?)

What is the length of a randomly selected five-year-old bluegill fish? 
Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is 
reduced by taking into account a quadratic function of the age of the fish.

file name "bluegills.py"

"""

# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Bluegill (Polynomial Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()



zz=np.array(5)
zz=zz.reshape(1,1)
print ("Predicting result with Linear Regression :"+str(lin_reg.predict(zz)))


print ("Predicting result with Polynomial Regression :"+str(lin_reg_2.predict(poly_reg.fit_transform(zz))))