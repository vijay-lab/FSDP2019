# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:45:14 2019

@author: TAPAN
"""

import re

phonebook = open("simpsons_phone_book.txt")
# iterating through every line in phonebook
for line in phonebook:
    if re.search("J.*Neu",line):#searching for keyword in every line
        print(line.rstrip())
phonebook.close()