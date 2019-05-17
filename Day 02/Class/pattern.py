"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 

"""

# Enter Number to print pattern
num = int(input("Enter Number to print Pattern: "))

# Prints the upper half of the pattern
for i in range(1,num+1):
    print("*" * i)

# Prints the lower half of the pattern
for i in range(num-1,0,-1):
    print("*" * i)
    
    
