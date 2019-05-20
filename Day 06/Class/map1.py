
"""
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.

"""

import random

names = ['Mary', 'Isla', 'Sam']

secret_names = list(map(lambda x: random.choice(['Mr. Pink',
                                            'Mr. Orange',
                                            'Mr. Blonde']),
                   names))