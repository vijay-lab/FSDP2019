# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:24:38 2019

@author: TAPAN
"""

"""

Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

kch_df=pd.read_csv('kc_house_data.csv')

features=kch_df.iloc[:,0:-1].values
label=kch_df.iloc[:,-1].values