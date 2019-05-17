
import re

input_str=input("Enter an string to verify")

#pattern = re.compile(r'[+-]\d{1,}\.\d{1,}')

if re.match(r'[+-]?\d{1,}\.\d{1,}',input_str):
    print(True)

else:
    print(False)

