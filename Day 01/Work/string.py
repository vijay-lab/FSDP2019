# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:33:35 2019

@author: TAPAN
"""

string=input("Enter the string you want it in reverse::")#took string from user
indr=string.find(" ")#finding index where space is present

print(string[indr+1:],string[:indr])#printing string from space +1 index to end then begning to space index