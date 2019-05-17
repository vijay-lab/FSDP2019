# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:29:39 2019

@author: TAPAN

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
# FOR SQLITE
import sqlite3
from pandas import DataFrame


est_conn= sqlite3.connect("university_rtu.db")


c = est_conn.cursor()




c.execute ("""CREATE TABLE students(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_no TEXT,
          Student_Branch TEXT
          )""")


c.execute("INSERT INTO students VALUES ('TAPAN', 22, '14EDACS045','CSE')")
c.execute("INSERT INTO students VALUES ('VIKAS', 21, '16EDACS044','CSE')")
c.execute("INSERT INTO students VALUES ('YASH', 20, '16EDACS045','CSE')")
c.execute("INSERT INTO students VALUES ('DIGVIJAY', 19, '16EDACS013','CSE')")
c.execute("INSERT INTO students VALUES ('VISHAL', 21, '16EDAEC009','ECE')")
c.execute("INSERT INTO students VALUES ('VIJAY', 21,'16EDACS044','CSE')")
c.execute("INSERT INTO students VALUES ('NITESH', 21, '16EDAEC063','IT')")
c.execute("INSERT INTO students VALUES ('PARESH', 26, '16EDAEC085','ELE')")
c.execute("INSERT INTO students VALUES ('ANUPAM', 23, '16EDAEC056','ME')")
c.execute("INSERT INTO students VALUES ('SOURABH', 03, '16EDAEC041','CSE')")
c.execute("INSERT INTO students VALUES ('HARSHIT', 15, '16EDAEC030','ARCH')")



c.execute("SELECT * FROM students")



df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Name","Age","Roll_No","Branch"]


# STEP 6
# commits the current transaction 
est_conn.commit()

# STEP 7
# closing the connection 
est_conn.close()







#For Mongo DB LOCAL

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# create the database if does not exists
mydb = client.university_rtu



# adding the employee in the employee collection
def add_student(Name, Age, Roll_no, Branch):
    unique_student = mydb.students.find_one({"Roll_no":Roll_no})
    if unique_student:
        return "Student already exists"
    else:
        mydb.employees.insert(
                {
                "Name" : Name,
                "Age" : Age,
                "Roll_no" : Roll_no,
                
                "Branch" : Branch
                })
        return "Student added successfully"

def fetch_all_students():
    user = mydb.students.find()
    for i in user:
        print (i)



add_student('TAPAN', 22, '14EDACS045','CSE')
add_student('TAPAN', 22, '14EDACS045','CSE')
add_student('VIKAS', 21, '16EDACS044','CSE')
add_student('YASH', 20, '16EDACS045','CSE')
add_student('DIGVIJAY',19,'16EDACS013','CSE')
add_student('VISHAL', 21, '16EDAEC009','ECE')
add_student('VIJAY', 21,'16EDACS044','CSE')
add_student('NITESH', 21, '16EDAEC063','IT')
add_student('PARESH', 26, '16EDAEC085','ELE')
add_student('ANUPAM', 23, '16EDAEC056','ME')
add_student('SOURABH', 3, '16EDAEC041','CSE')
add_student('HARSHIT', 15, '16EDAEC030','ARCH')


fetch_all_students()






