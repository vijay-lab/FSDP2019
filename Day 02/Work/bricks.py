"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""

def make_bricks(small, big, goal):
    if goal % 5 > small:
        print (False) 
    else:    
        c = big*5 + small
        if c >= goal:
            print (True)
        else:
            print (False)

lst = input("Enter Numbers: ").split(",")

my_list=[]

for i in lst:
    my_list.append(int(i))
    
make_bricks(my_list[0], my_list[1], my_list[2])