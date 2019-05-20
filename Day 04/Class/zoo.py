"""
Hands On  1
  Read the zoo.csv file using the csv library and print each row
Hands On  2
  Read the zoo.csv file using the csv library and print each columns
Hands On  3
  Read the zoo.csv file using the csv library and print the total water needed 
  by all the animals
Hands On  4
  Read the zoo.csv file using the csv library and print the total water needed
  by all the animals by grouping
Hands On  5
  Read the zoo.csv file using the csv library and print the total water needed 
  by all the animals by grouping using dictionary 



 Reading from a .csv file into Dictionary

file_name - 'zoo.py'

  """


# Hands On 1
import csv

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        print (row)
        
# Hands On 2
import csv

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for column in csv_reader:
        for i in range(len(column)):
            print (column[i])
            
# Hands On 3
import csv

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed = 0
    # Use the below line to skip the header line from the csv file 
    next(csv_reader) 
    for column in csv_reader:
        total_water_needed = int(column[2])+total_water_needed

print ("Total water needed by all the animals : "+str(total_water_needed))

# Hands On 4
import csv

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed_elephant = 0
    total_water_needed_tiger = 0
    total_water_needed_zebra = 0
    total_water_needed_lion = 0
    total_water_needed_kangaroo = 0


    # Use the below line to skip the header line from the csv file 
    next(csv_reader) 
    for column in csv_reader:
        if column[0]=="elephant":
            total_water_needed_elephant = int(column[2])+total_water_needed_elephant
        if column[0]=="tiger":
            total_water_needed_tiger = int(column[2])+total_water_needed_tiger
        if column[0]=="zebra":
            total_water_needed_zebra = int(column[2])+total_water_needed_zebra
        if column[0]=="lion":
            total_water_needed_lion = int(column[2])+total_water_needed_lion
        if column[0]=="kangaroo":
            total_water_needed_kangaroo = int(column[2])+total_water_needed_kangaroo


print ("Total water needed by aelephant : "+str(total_water_needed_elephant))
print ("Total water needed by tiger : "+str(total_water_needed_tiger))
print ("Total water needed by zebra : "+str(total_water_needed_zebra))
print ("Total water needed by lion : "+str(total_water_needed_lion))
print ("Total water needed by kangaroo : "+str(total_water_needed_kangaroo))

# Hands On 5
import csv

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed_elephant = 0
    total_water_needed_tiger = 0
    total_water_needed_zebra = 0
    total_water_needed_lion = 0
    total_water_needed_kangaroo = 0


    # Use the below line to skip the header line from the csv file 
    next(csv_reader) 
    for column in csv_reader:
        if column[0]=="elephant":
            total_water_needed_elephant = int(column[2])+total_water_needed_elephant
        if column[0]=="tiger":
            total_water_needed_tiger = int(column[2])+total_water_needed_tiger
        if column[0]=="zebra":
            total_water_needed_zebra = int(column[2])+total_water_needed_zebra
        if column[0]=="lion":
            total_water_needed_lion = int(column[2])+total_water_needed_lion
        if column[0]=="kangaroo":
            total_water_needed_kangaroo = int(column[2])+total_water_needed_kangaroo
            
animal_dictionary = {}

animal_dictionary["elephant"]=total_water_needed_elephant
animal_dictionary["tiger"]=total_water_needed_tiger
animal_dictionary["zebra"]=total_water_needed_zebra
animal_dictionary["lion"]=total_water_needed_lion
animal_dictionary["kangaroo"]=total_water_needed_kangaroo

print (animal_dictionary)