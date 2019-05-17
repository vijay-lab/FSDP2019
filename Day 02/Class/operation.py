"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

def Add(lst):
    total = 0
    for i in lst:
        total += i
    return total

def Multiply(lst):
    product = 1
    for i in lst:
        product *= i
    return product

def Largest(lst):
    init = lst[0]
    for i in lst:
        if init < i:
            init = i
    return init

def Smallest(lst):
    init = lst[0]
    for i in lst:
        if init > i:
            init = i
    return init

def Sorting(lst):
    s = len(lst)
    us = True
    while us:
        us = False
        i = 0
        while i<s-1:
            if lst[i] > lst[i+1]:
                t = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = t
                us = True
            i += 1
    return lst

def Remove_Duplicates(lst):
    n_lst = []
    for i in lst:
        if i not in n_lst:
            n_lst.append(i)
    return n_lst

def Print(lst):
    lst = list(lst)
    print (Add(lst))
    print (Multiply(lst))
    print (Largest(lst))
    print (Smallest(lst))
    print (Sorting(lst))
    print (Remove_Duplicates(lst))

my_list = input("Enter list: ").split(",")

final_list = []

for i in my_list:
    final_list.append(int(i))
    
Print (final_list)
