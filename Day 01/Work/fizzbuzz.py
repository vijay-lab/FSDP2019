# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:14:52 2019

@author: TAPAN
"""



count = 0
while (count< 100):
    count = count + 1
    if (count%3 == 0 and count%5 == 0 ):
        print("FizzBuzz")
        continue
    elif(count%3 == 0):
        print("Fizz")
        continue
    elif(count%5 == 0):
        print("Buzz")
        continue
    
        
    print(count)
        
    
    