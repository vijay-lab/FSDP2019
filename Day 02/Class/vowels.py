"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = list('aeiou')

final_list = []

for state in state_name:
    state_elements = list(state.lower())
    
    for element in vowels:
        while element in state_elements:
            state_elements.remove(element)
    final_list.append("".join(state_elements))

print (final_list)


