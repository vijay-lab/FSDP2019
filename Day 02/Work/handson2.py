# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:52:34 2019

@author: TAPAN
"""

Year=int(input("Enter a year you want to test\n"))

#if (Year%4==0 and Year%100!=0 ):
#    
#    print ("it's a leap year")
#
#
#elif(Year%100==0 and Year%400==0 ):
#    print ("it's a leap year")
#
#    
#else:
#    print ("not a leap year")
    
def leap_year(year):
    
    
    return Year%4==0 and (Year%100!=0 or Year%400==0)

print(leap_year(Year))