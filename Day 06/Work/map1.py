# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:32:29 2019

@author: TAPAN
"""
#j=0
#def comp(x):
#    j=len(names)
#    if names[i] is names[-j+1]:
#        names[i]=random.choice(code_names)
#        j=j+1
#    return names[i]
#    
names = ['Mary', 'Isla', 'Sam',]
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']



import random 

def comp(x):
    length=len(names)
    for i in range(length):
        val = random.randint(0,len(names) -i-1)
        
        names[i] = code_names.pop(val)
    
    return names
    



result = map(comp, code_names) 
result=list(result) 




result=result.pop(0)
print(result)