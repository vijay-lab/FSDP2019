# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:57:25 2019

@author: TAPAN
"""

tup_db= ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

input_days=input("Enter Days you want to add to the list in CSV Format").split(',')

for day in tup_db:
    if day not in input_days:
        input_days.append(day)

print(tuple(input_days))
