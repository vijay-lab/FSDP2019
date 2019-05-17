# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:12:39 2019

@author: TAPAN
"""

ls1=[12,24,35,24,88,120,155,88,120,155]


ls2=[]

for item in ls1:
    if item not in ls2:
        ls2.append(item)
        
print(ls2[::-1])