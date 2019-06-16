# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:11:29 2019

@author: TAPAN
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

# Importing the dataset
insurence_df = pd.read_csv('insurence.csv',index_col=[0])# read index 0 as index
 
drop_list=np.where(insurence_df['job']=='unknown')
insurence_df.isnull().any(axis=0)
insurence_df['job'].value_counts()

# cleaned unknown data
for i in drop_list:
    insurence_df=insurence_df.drop(i)



features=insurence_df.iloc[:,:-1]
label=insurence_df.iloc[:,-1]
le=LabelEncoder()
features['job']=le.fit_transform(features['job'])




