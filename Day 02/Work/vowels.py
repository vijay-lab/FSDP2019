# -*- coding: utf-8 -*-
"""
Created on Thu May 23 07:54:40 2019

@author: TAPAN
"""

vowel_free=[]
state_name = ['Alabama','California','Oklahoma', 'Florida']
vowels=['a','e','i','o','u']

for state in state_name:
    state_elements = list(state.lower())
    
    for vowel in state_elements:#vowel
        if vowel in vowels:#state elem
            state_elements.remove(vowel)
            
    vowel_free.append("".join(state_elements))

        
print(vowel_free)

