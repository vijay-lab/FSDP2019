"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
  Input: 
    12 9 61 5 14
  Output:
    True
"""

user_input = input("Enter space seperated values :").split()

input_length  = len(user_input)
count = 0
pallindromic_integer = False

for num in user_input:
    if int(num) > 0:
        count += 1

if count == input_length:
    for positive_num in user_input:
        if positive_num == positive_num[::-1]:
            pallindromic_integer = True

print(pallindromic_integer)


# Short Logic using the all and any keyword

# give list of inputs from user
user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
    