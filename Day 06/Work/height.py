# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:30:04 2019

@author: TAPAN
"""

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0

for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

print (average_height)
    
    



from functools import reduce


print (reduce (lambda x,y : x + y,[2,18,9,22,17,24,8,12,27]))


def f(x) :
    return x%3 ==0 or x%5 ==0 


my_list = list(range(2,25 ))
print(my_list)

my_filter_list = filter ( f, my_list)
print(list(my_filter_list))

# Filter with Lambda function 
my_filter_list = filter ( lambda x:x%3==0 or x%5==0, my_list)
print(list(my_filter_list))

filter>>reduce