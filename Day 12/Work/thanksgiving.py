# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:50:28 2019

@author: TAPAN
"""

import pandas as pd



tg_df=pd.read_csv("thanksgiving.csv",encoding='Windows-1252')


columns = list(tg_df.columns)

columns[0:11]
len(tg_df.columns)