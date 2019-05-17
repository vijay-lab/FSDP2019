# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:31:32 2019

@author: TAPAN
"""

A1=int(input("Enter Marks for assignment 1 "))#Taking Assignment marks from user
A2=int(input("Enter Marks for assignment 2 "))
A3=int(input("Enter Marks for assignment 3 "))
E1=int(input("Enter Marks for exam 1 "))#Taking Assignment marks from user
E2=int(input("Enter Marks for exam 2 "))


weighted_score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35 # formula to calculate weighted score 

print("Weighted score of all the assignment & exam is",weighted_score)#printing weighted score 