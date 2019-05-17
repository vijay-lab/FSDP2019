"""
Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 50(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples 
    of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
    User Input not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

for i in range(1,100):
    
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)