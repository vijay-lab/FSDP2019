"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

file = open('absent_students.txt','w')
file.close()

with open('absent_students.txt','a') as file:
    for i in range(25):
        absent_student_name = raw_input("Enter the absent student name: ")
        if absent_student_name=="":
            break
        file.write(absent_student_name+'\n')
        

file = open('absent_students.txt','r')
print file.readlines()
    