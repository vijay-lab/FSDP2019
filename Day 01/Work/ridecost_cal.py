# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:23:37 2019

@author: TAPAN
"""

Fuel_avg=18#Milege of the car

dis_to_office=80#total distance from office to home & vice- versa

cost_diesel=80#current price of diesel

tot_fuel_consumed=dis_to_office/Fuel_avg


print("Total Fuel Consumed"  )

print(tot_fuel_consumed)

commuting_cost=tot_fuel_consumed*cost_diesel

print("Total Cost to commute from office to home and vice-versa")

print (commuting_cost)