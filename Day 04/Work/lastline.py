# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:31:35 2019

@author: TAPAN
"""

name_file=input("Enter the name of the file") +'.txt'

fp = open(name_file,"rt")

data=fp.readlines()