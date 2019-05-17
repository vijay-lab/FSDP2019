# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:37:20 2019

@author: TAPAN
"""


    
with open('words.txt', mode='rt') as file_old :
    with open('file_new.txt', mode='wt') as file_new :
        for line in file_old:
            file_new.write(line)