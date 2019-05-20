 
users = {} 
with open('data/passwd') as f:
    for line in f:
        if not line.startswith("#"):
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]
 
for username in sorted(users):
    print("{}:{}".format(username, users[username]))
 

# Discussion


""" 
The above program uses one of the most common actions done in a Python program: 
We open a file, and then iterate over the contents of that file, line by line, 
doing something with each line. In this particular case, we're splitting each line
into fields across the : character, using the str.split method. str.split always 
returns us a list, although the length of that list depends on the number of times 
that : is contained. In the case of /etc/passwd, we can assume that any line 
containing : is a legitimate user record, and thus has all of the necessary fields.
 
However, the file might contain comment lines beginning with #. 
If we were to invoke str.split on those lines, we would get back a list, 
but one containing only a single element---leading to an IndexError exception 
if we would try to retrieve user_info[2]. It is thus important that we ignore 
those lines that begin with #. Fortunately, there is a str.startswith method, 
which returns True if the line starts with the string passed as an argument. 
By negating this (if not line.startswith("#")), we can be sure that we're only 
splitting line for legitimate lines.
 
Assuming that it has found a user record, our program then adds a new 
key-value pair to users. The key is user_info[0], and the value is user_info[2]. 
Notice how we can use user_info[0] as the name of a key; so long as the value 
of that variable contains a string, we may use it as a dictionary key.
 
The use of with, known as a "context manager" within Python, is somewhat 
unnecessary here, and in many short programs. When used with a file object, 
with automatically handles the closing of our file when the block ends, 
as opposed to waiting until the end of the program.
 
A slight issue with the above program, if you are an experienced Python programmer, 
is the use of the for loop to construct a dictionary. 
We could used instead a dictionary comprehension to turn the file into a dictionary,
 which---to my mind, at least---is a cleaner way to do things, 
 if less obvious to Python newcomers. 
 
 The equivalent to our for loop is:
 
users =  { line.split(':')[0] : line.split(':')[2] for line in open('/etc/passwd') 
if not line.startswith('#') } 
 
I love dictionary comprehensions, although I recognize that it's sometimes hard 
to put all of the functionality inside of them. 
Furthermore, their syntax can be a bit off-putting to less experienced Python 
developers.  This dict comprehension takes advantage of the fact that we can 
iterate over the lines of /etc/passwd. Each line can then be checked whether 
it begins with #; if it doesn't, then we split the line across :, 
and return thedictionary with name-ID pairs.
 
Once we have finished creating our dictionary, we must iterate over it and 
print each key-value pair. When we iterate over a dictionary, we're actually 
iterating over its keys---and thus, a for loop on a dictionary will return its keys, 
one at a time. We can invoke the built-in sorted function, passing it the dictionary 
as its argument, which returns a list of the dictionary's keys. 
This list thus becomes the collection over which our for loop operates, 
allowing us to print the usernames in alphabetical order, along with the user IDs.
"""
