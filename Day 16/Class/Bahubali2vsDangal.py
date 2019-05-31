"""
Import Bahubali2vsDangal.csv file.

It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
(in crores) for the first 9 days. Now, you have to write a python code to 
predict which movie would collect more on the 10th day.

file name "Bahubali2vsDangal.csv"

"""

import pandas as pd
import matplotlib.pyplot as plt

#Importing 12.828
dataset = pd.read_csv("Bahubali2_vs_Dangal.csv")

#print dataset.describe()
x1 = dataset.iloc[:, 0:1].values
y1 = dataset.iloc[:, 1:2].values   # Bahubali 2
y2 = dataset.iloc[:, 2:3].values   # Dangal

from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(x1, y1) #convert into 2d array

regressor2 = LinearRegression()
regressor2.fit(x1, y2) #convert into 2d array

day = input("Enter Day to Check Collection: ")

y1_pred = regressor1.predict(day)
print ("Bahubali 2 earns on {0}th day :".format(day))
print (y1_pred)
y2_pred = regressor2.predict(day)
print ("Dangal earns on {0}th day :".format(day))
print (y2_pred)

plt.plot(x1, y1, color = 'red',label="Bahubali 2")
plt.plot(x1, y2, color = 'green', label="Dangal")
plt.scatter(day, regressor1.predict(day), color = 'red',s=300)
plt.scatter(day, regressor2.predict(day), color = 'green',s=300)
plt.title('Bahubali 2 vs Dangal')
plt.xlabel('Day')
plt.ylabel('Collection')
plt.legend()
plt.show()

if y1_pred > y2_pred:
 print ("Therefore, Bahubali 2 will earn more on the {0}th day".format(day))
else:
 print ("Therefore, Dangal will earn more on the {0}th day".format(day))