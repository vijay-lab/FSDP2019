"""
You will implement linear regression to predict the profits for a food chain 
company.

Case: Suppose you are the CEO of a restaurant franchise and are considering 
different cities for opening a new outlet. 
The chain already has food-trucks in various cities and you have data for 
profits and populations from the cities. You would like to use this data to 
help you select which city to expand to next. 

Foodtruck.csv contains the dataset for our linear regression problem. 
The first column is the population of a city and the second column is the 
profit of a food truck in that city. A negative value for profit indicates a 
loss.

Perform Simple Linear regression to predict the profit based on the population
 observed and visualize the result.
Based on the above trained results, what will be your estimated profit, 
if you set up your outlet in Jaipur? 
(Current population in Jaipur is 3.073 million)

Filename "Foodtruck.py"

"""

import pandas as pd
import matplotlib.pyplot as plt

#Importing 12.828
dataset = pd.read_csv("Foodtruck.csv")
#print dataset.describe()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Splitting
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#   Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results,compare it with y_test
y_pred = regressor.predict(X_test)
print (y_pred)


# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'red')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()