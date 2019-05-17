"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) 0.1 + (E1 + E2 )  0.35
"""
# Enter marks for assignments 
a1 = int(input("Enter Marks for Assignment 1: "))
a2 = int(input("Enter Marks for Assignment 2: "))
a3 = int(input("Enter Marks for Assignment 3: "))

# Enter marks for exams
e1 = int(input("Enter Marks for Exam 1: "))
e2 = int(input("Enter Marks for Exam 2: "))

# Calculating weighted_score
weighted_score = ( a1 + a2 + a3 ) * 0.1 + (e1 + e2 ) *  0.35

print("Weighted Score is " + str(weighted_score))