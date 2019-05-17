# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:54:16 2019

@author: TAPAN
"""
Year, month=input("Enter a year and month you want to test\n").split()
days_in_month= [31,28,31,30,31,30,31,31,30,31,30,31]
def leap_year(year):
    
    
    return Year%4==0 and (Year%100!=0 or Year%400==0)

print(leap_year(Year))


def days_in_month(month):
    
    if month>=1 and month <=12:
        return 'INvalid month'
    
    if month == 2 and leap_year(Year):
        return 29
    
    