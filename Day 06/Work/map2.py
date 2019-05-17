# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:55:14 2019

@author: TAPAN
"""

names = ['Mary', 'Isla', 'Sam']

def hash_maker(name):
    
    for i in range(len(names)):
        names[i] = hash(names[i])
    return names

hash_maker(names)



names = ['Mary', 'Isla', 'Sam','Tapan']

hashed_values=list(map( lambda name : hash(name),names))

print(hashed_values)
