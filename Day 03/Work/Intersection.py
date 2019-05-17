# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:05:48 2019

@author: TAPAN
"""

ls1=[1,3,6,78,35,55] 
ls2=[12,24,35,24,88,120,155]

sls1=set(ls1)
sls2=set(ls2)

ls3=sls1.intersection(ls2)

print(list(ls3))