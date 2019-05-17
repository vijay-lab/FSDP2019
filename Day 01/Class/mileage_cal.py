"""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilometers by the litres used to get the average
"""

# Enter km car travels
travel_km = float(input("Enter car travel distance in Km >"))

# Enter fuel consumption value in litres
fuel_litres = float(input("Enter Fuel consumption in litres >"))

# Average of the car
average_of_car = (travel_km/fuel_litres)

print ("Average of my car is :"+str(average_of_car))