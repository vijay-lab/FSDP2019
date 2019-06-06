# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:52:33 2019

@author: TAPAN

3.Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 

 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
 
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans


job_df = pd.read_csv('monster.csv')
ctr=['job_description','country','country_code','date_added','has_expired','job_board','page_url','uniq_id']
job_df=job_df.drop(ctr,axis=1)

job_df=job_df.dropna(subset=['organization'])



#job_df['location']=job_df['location'].str.split('[0-9]+',expand=True)
#job_df['organization']=job_df['organization'].str.split(',',expand=True)

match = re.search(',',str(job_df['organization']))

