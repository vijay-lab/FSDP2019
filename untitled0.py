# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:16:56 2019

@author: TAPAN
"""
import numpy as np
import pandas as pd


house_data=pd.read_csv("kc_house_data.csv")
house_data=house_data.drop('id',axis=1)

null_values=house_data.isnull().any(axis=0)
#splitting the date column
house_data['date']=house_data['date'].str.split('T0*',expand=True)



