# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:54:24 2019

@author: TAPAN
"""

import pandas as pd


df = pd.read_csv("training_titanic.csv")


survived =df['Survived'].value_counts()
sur=survived.tolist()
#How many people in the given training set survived the disaster ?
print("NO. of survived people is",sur[1])
print("No. of survived people",df['Survived'][df['Survived']==1].value_counts())


#How many people in the given training set died ?
print("NO. of Dead people is",sur[0])
print("No. of dead people",df['Survived'][df['Survived']==0].value_counts())



#Calculate and print the survival rates as proportions (percentage) 
survived_per =df['Survived'].value_counts(normalize=True)
print("No of dead people in %",survived_per[0])
print("No of survived people in %",survived_per[1])


#Males that survived vs males that passed away
df['Survived'][(df['Sex']=='male')].value_counts()

#Females that survived vs Females that passed away
df['Survived'][(df['Sex']=='female')].value_counts()


#  Does age play a role?
#  since it's probable that children were saved first.
#  
#  Another variable that could influence survival is age; 
#  since it's probable that children were saved first.
#
#  You can test this by creating a new column with a categorical variable Child. 
#  Child will take the value 1 in cases where age is less than 18, 
#  and a value of 0 in cases where age is greater than or equal to 18.

#  Then assign the value 0 to observations where the passenger 
#  is greater than or equal to 18 years in the new Child column.
#  Compare the normalized survival rates for those who are <18 and 
#  those who are older. 
#
#  To add this new variable you need to do two things
# 1.     create a new column, and
# 2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
df_new_child=df
df_new_child['Child'] = 0
df_new_child['Child'][(df_new_child['Age']<18)]=1


































    