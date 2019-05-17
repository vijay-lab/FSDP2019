"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""

input_string = input("Enter your String :")

replaced_char = input("Enter Character which you want to replace :")

replacement_char = input("Enter Character using which you want to replace :")

# First occurence of replaced character
first_occurence = input_string.find(replaced_char)

# Replace replaced character with replacement character from input string
print (input_string[:first_occurence+1] + input_string[first_occurence+1:].replace(replaced_char, replacement_char,1))

