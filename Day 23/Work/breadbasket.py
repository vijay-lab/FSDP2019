# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:33:07 2019

@author: TAPAN

Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on 
a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.


"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

basket = pd.read_csv('BreadBasket_DMS.csv') 

# 1.Draw the pie chart of top 15 selling items.
basket[basket['Item']=='NONE']=np.nan

values=basket['Item'].value_counts()[:15]
plt.pie(values,labels=values.index,autopct='%1.1f%%',radius=2)

# 2.
grpd_items=pd.Series(basket.groupby('Transaction')['Item'])

transactions=[]

for i in range(0,9465):
    transactions.append(list(grpd_items[i][1]))
 
from apyori import apriori

rules = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

results=list(rules)


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

# 3. to access seperate items
Ist_item=list(results[0][0])[0]

IIst_item=list(results[0][0])[1]
