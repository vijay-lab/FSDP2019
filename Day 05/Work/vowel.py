# -*- coding: utf-8 -*-
"""
Created on Sun May 12 22:43:25 2019

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

