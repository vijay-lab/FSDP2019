""" Code challenge to create a command to copy a file

file_name - 'copy_file.py'

"""

# copy 'words.txt' into 'abc.txt'

another_file = open('abc.txt','wt')
with open('words.txt','rt') as file:
    for text in file.readlines():
        another_file.write(text)
another_file.close()