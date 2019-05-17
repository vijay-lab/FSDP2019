# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:10:23 2019

@author: TAPAN
"""
import random as rn

rand_no=rn.randint(1,10)

input_val=None
count =0

while rand_no != input_val and count<6:
    count = count+1
    left= 6-count
    
    
    input_val=int(input("Enter a Number to check your gueeing power::"))
    if rand_no != input_val:
        print("You loose")
        if(rand_no<input_val):
            print("Too High","Tries left=",left)
            
            
        elif(rand_no> input_val):
            print("Too Low","Tries left=",left)
while left ==0:
    rep=input("Do you want to play Again")
if (rep =='y' or 'Y' or 'YES' or 'yes' or 'Yes'):
    
            

        
    else:
        print("Player Wins")
        break
    