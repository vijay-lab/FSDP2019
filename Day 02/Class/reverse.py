"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
# Function to reverse a string
def reverse(input_string):
	# Reverse String
	return (input_string[::-1])

input_string = input("Enter a string >")
print (reverse (input_string))

