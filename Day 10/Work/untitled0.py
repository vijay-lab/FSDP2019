# -*- coding: utf-8 -*-
"""
Created on Thu May 23 22:57:09 2019

@author: TAPAN
"""

import pandas as pd
df= pd.read_csv('pokemon_data.csv')

# read headers
df.columns
df['Name'][0:3]
df[['Name','Type 1','Type 2']]
#read row
df.iloc[1:4]

df[df['Type 1']=='Fire']