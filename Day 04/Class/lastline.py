
filename = input("Enter a filename: ")
print(open(filename).readlines()[-1])

# Explanation / Discussion:

"""
The above uses a number of common Python expressions. 
First and foremost, it's important to remember that when you open a file, 
you're creating a file object. 
This object is often put into a variable:
"""
 
f = open(filename)
 
"""
But it doesn't have to be put into a variable. 
And in fact, if you're just planning to iterate over a file, 
then there's not necessarily any reason to set a variable. 
In this particular case, 
 Now, it's typical in Python to iterate with a for loop over the contents of a 
file, as in: 
"""
 
for line in open(filename):
    print(len(line))
 
"""
But you don't *have* to iterate over the lines of a file. 
If you're working with binary files, then the concept of a "line" in the file 
is nonsensical.
"""
 
"""
In this particular exercise, you were asked to print the final line of a file.
One way to do this might be:
"""
 
for line in open(filename):
    pass
 
"""
The above trick works because we iterate over the lines of the file and 
assign line in each iteration---but we don't actually do anything in the body 
of the for loop. 
Rather, we use pass, which is a way of telling Python to do nothing. 
The reason that we execute this loop is for its side effect---namely, 
the fact that the final value assigned to line remains in place after the 
loop exits.
"""

"""
However, looping over the rows of a file just to get the final one strikes me 
as a bit wasteful and unnecessary. 
My preferred solution, as outlined above, is to turn the file into a list of strings, 
with one line per list element. 
Thus, the first row of the file will be at index 0, the second line at index 1, 
and so forth. 
But in Python, we can retrieve the final line of a file with index -1. 
Thus, if we turn the file into a list of strings, and then retrieve the element at index -1, 
we have actually retrieved the final line of the file.
"""

"""
The downside of this approach is that we actually need to create a list from all of the rows of the file. 
This can potentially suck up a great deal of memory. 
If you're going to work with a large file, then the use of pass in the above example might actually be more efficient in terms of memory usage.
"""

