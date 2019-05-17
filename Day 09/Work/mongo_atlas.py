# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:23:46 2019

@author: TAPAN
"""

import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")


client = pymongo.MongoClient("mongodb://Tapan:Vijay@projectm-shard-00-00-xxtny.mongodb.net:27017,projectm-shard-00-01-xxtny.mongodb.net:27017,projectm-shard-00-02-xxtny.mongodb.net:27017/test?ssl=true&replicaSet=ProjectM-shard-0&authSource=admin&retryWrites=true")
db = client.test

mydb = client.ProjectM

def add_student(Name, Age, Roll_no, Branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.ProjectM.insert_one(
             {
                "Name" : Name,
                "Age" : Age,
                "Roll_no" : Roll_no,
                "Branch" : Branch
                })  
    return "Student added successfully"


def fetch_all_students():
    user = mydb.ProjectM.find()
    for i in user:
        print (i)



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

