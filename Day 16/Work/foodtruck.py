# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:59:28 2019

@author: TAPAN


Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ft_df=pd.read_csv("Foodtruck.csv")


plt.boxplot(ft_df.values)

ft_df.plot(x='Population', y='Profit', style='o')  
plt.title('Population vs Profit')  
plt.xlabel('Population ')  
plt.ylabel('Profit ')  
plt.show()

features = ft_df.iloc[:, :-1].values  
labels = ft_df.iloc[:, 1].values 

"""
train the model now 
"""

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features, labels) 

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)

jaipur=np.array(3.073).reshape(1,1)

print ("The Profit by opening a store in jaipur is",round(regressor.predict(jaipur)[0],4),"i.e. it's a loss to expend in jaipur")





