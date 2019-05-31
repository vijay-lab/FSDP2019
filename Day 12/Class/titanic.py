"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Problem Statement:
      It’s a real-world data containing the details of titanic ships passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of a DataFrame
      
      You can test this by creating a new column with a categorical variable Child.
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.  

      Then assign the value 0 to observations where the passenger is 
      greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and those who are older. 
   
"""
import pandas as pd

data = pd.read_csv('data/training_titanic.csv')

data.shape

data.info()

data.head(10)

data['Survived'].value_counts()


disaster_survived = data['Survived'].value_counts()[1]

disaster_died = data['Survived'].value_counts()[0]

disaster_survived_percentage = data['Survived'].value_counts(normalize=True)[1]

disaster_died_percentage = data['Survived'].value_counts(normalize=True)[0]

male_survived = data['Survived'][data['Sex'] == 'male'].value_counts(normalize=True)[1]
male_passed_away =  data['Survived'][data['Sex'] == 'male'].value_counts(normalize=True)[0]

female_survived = data['Survived'][data['Sex'] == 'female'].value_counts(normalize=True)[1]
female_passed_away =  data['Survived'][data['Sex'] == 'female'].value_counts(normalize=True)[0]


print ("disaster_survived : "+str(disaster_survived))
print ("disaster_died : "+str(disaster_died))
print ("disaster_survived_percentage : "+str(round(disaster_survived_percentage*100,2))+"%")
print ("disaster_died_percentage : "+str(round(disaster_died_percentage*100,2))+"%")
print ("male_survived : "+str(round(male_survived*100,2))+"%")
print ("male_passed_away : "+str(round(male_passed_away*100,2))+"%")
print ("female_survived : "+str(round(female_survived*100,2))+"%")
print ("female_passed_away : "+str(round(female_passed_away*100,2))+"%")


data['Child'] = 0
data['Child'][data['Age'] < 18] = 1
c =  data['Survived'][data['Child'] == 1].value_counts(normalize=True)
print ("Child Survived : "+str(round(c[1]*100, 2))+"%")



"""
Another way try this using map function  
"""
survived['Child']=df['Age'].map({'Female':0,'Male':1})





""" 
Program to add an emopty column Child and fill the values by 1 if
age is >18 and by 0 if age is <18
"""

# Adding the column Child with values 0 in the existing dataframe stored in df_mod
data['Child'] = 0

# Filling the empty numerical columns
data = data.fillna(data.mean())

# Filling child column with 1 where age is greater than 18
data['Child'][data['Age'] > 18] = 1

# to use .apply method on a dataframe
# To create a dataframe where we have to fill 1 for age less than 18 and 0 for more than 18
a = data.loc[:, ['Age']]
a['Child'] = 'mising'


# A function to be passed in apply method for performing the above operation
def filter_data(value):
    if 0 <= value <= 18:
        return 1
    else:
        return 0


a['Child'] = a['Age'].apply(filter_data)








