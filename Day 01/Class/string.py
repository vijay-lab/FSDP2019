"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  them in reverse order with a space between them, find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""

# Take name as input from user
name = input("Enter your name with lastname :")

# Find index for space
space_index = name.index(' ')  # or use find function 

print (name[space_index+1:]+' '+name[0:space_index+1])

