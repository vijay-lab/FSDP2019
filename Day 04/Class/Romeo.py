# -*- coding: utf-8 -*-

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

# To open the file
with open("romeo.txt", "rt") as fileobj:

    content = fileobj.readlines()
    
    # List to hold the list of the words
    req_content = []
    for var in content:
        req_content.append(var.split())
    
    # To count the words using dictionary
    dict1 = {}
    for var2 in req_content:
        for var3 in var2:
            if var3 not in dict1:
                dict1[var3] = 1
            else:
                dict1[var3]+=1
            
        