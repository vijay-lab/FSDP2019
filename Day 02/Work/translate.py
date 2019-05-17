
"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate the text as mentioned. 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

def translate(string):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    final_list = []

    for element in string:
        if element in consonants: 
            final_list.append(element+"o"+element)
        else:
            final_list.append(element)

    return "".join(final_list)

user_input = input("Enter string to Translate: ")

print (translate(user_input))

