# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:02:51 2019

@author: TAPAN
"""

from bs4 import BeautifulSoup
import requests



host_url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
host = requests.get(host_url).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(host,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='table')

print (right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll('tr'):
    column = row.findAll('td')
    if len(column) == 5:
        A.append(column[0].text.strip())
        B.append(column[1].text.strip())
        C.append(column[2].text.strip())
        D.append(column[3].text.strip())
        E.append(column[3].text.strip())
        
        
        
import pandas as pd
from collections import OrderedDict

col_name = ["Position","country","weighted matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

df = pd.DataFrame(col_data)
df.to_csv("icc.csv",index=False)