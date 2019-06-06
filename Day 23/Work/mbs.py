# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:51:05 2019

@author: TAPAN

Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values
 from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.

"""

# Apriori

# Importing the libraries
import pandas as pd
import numpy as np
from apyori import apriori
import matplotlib.pyplot as plt

# Data Preprocessing
mbs = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

mbs1=mbs.replace(to_replace =np.NaN, value ="None") 

transactions = []
temp=[]
for i in range(7501):
    for j in range(20):
        if (mbs1.values[i,j] == 'None'):
            continue
        else:
            temp.append(mbs1.values[i,j])
    transactions.append(temp)
    temp = []
    

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    
frequency=[]
i=1
for i in range(20):
    frequency.append(mbs[i].value_counts())
    i+=1
    
frame=frequency[0] | frequency[1] |frequency[2] | frequency[3]
    
if (frequency[0].index is frequency[1].index  ):
    
    
    

    
    
    
    
    