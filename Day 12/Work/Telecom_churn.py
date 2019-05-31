# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:05:30 2019

@author: TAPAN


    Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
        
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?

    
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


telco_df = pd.read_csv("Telecom_churn.csv")


churn_df=telco_df[(telco_df['international plan']=='yes') & (telco_df['voice mail plan']=='yes')]

print(churn_df['churn'].value_counts(normalize=True))

# Total charges for international calls made by churned and non-churned customer and visualize it

# Code for customers who has international voice plan and are churned customer too .
vis=[]
ic_t=telco_df[(telco_df['international plan']== 'yes' ) & (telco_df['churn']== True)]
vis.append(ic_t['total intl charge'].sum())

# Code to find customers who has international voice plan and aren't churned customer. 

ic_t=telco_df[(telco_df['international plan']== 'yes' ) & (telco_df['churn']== False)]
vis.append(ic_t['total intl charge'].sum())


labels = 'Churned cust', 'Unchurned Cust'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0)  # explode 1st slice
#plotting the data intoo pie chart.
plt.pie(vis, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)

plt.title('\nCustomers with International Plan Enabled')

#3. Predict the state having highest night call minutes for churned customer
churn_true = telco_df[telco_df['churn'] == True]
max_call=churn_true['total night minutes'].max()
telco_df['state'][(telco_df['total night minutes']==max_call)]


#4. Visualize -
#    a. the most popular call type among churned user
call_type_pop=[]
call_type_pop.append(churn_true['total day calls'].value_counts())
call_type_pop.append(churn_true['total eve calls'].sum())
call_type_pop.append(churn_true['total night calls'].sum())
explode11=(0.5,0,0)
labels= 'Day callls','Evening Calls','Night Calls'
plt.title('\nFav. call type among churned Customers ' )

plt.pie(call_type_pop, explode=explode11, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)
plt.show()
#    b. the minimum charges among all call type among churned user


call_type_least=[]
call_type_least.append(churn_true['total day calls'].sum())
call_type_least.append(churn_true['total eve calls'].sum())
call_type_least.append(churn_true['total night calls'].sum())
explode11=(0,0,0.3)
labels= 'Day callls','Evening Calls','Night Calls'
plt.title('\nFav. call type among churned Customers ' )

plt.pie(call_type_least, explode=explode11, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)
plt.show()


#5. Which category of customer having maximum account lenght? Predict and print it
churn_false_no = telco_df['account length'][telco_df['churn'] == False].max()

churn_true_no = churn_true['account length'].max()
if (churn_true_no > churn_false_no):
    print('churned user have bigger a/c length and it is::',churn_true_no)
else:
    print('Non churned user have bigger a/c length and it is::',churn_false_no)

#6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not

customer_care_churn = churn_true['customer service calls'].value_counts()
