
 
filename = input("Enter a filename: ")
 
number_of_characters = 0
number_of_words = 0
unique_words = set()
 
for number_of_lines, line in enumerate(open(filename), 1):
    number_of_characters += len(line)
    number_of_words += len(line.split())
    unique_words.update(line.split())
 
print("Number of lines: {}".format(number_of_lines))
print("Number of characters: {}".format(number_of_characters))
print("Number of words: {}".format(number_of_words))
print("Number of unique words: {}".format(len(unique_words)))
 

"""Discussion
 
This program demonstrates a number of aspects of Python that many programmers use on a daily basis.
 
First and foremost, the goal of this program is to count aspects of the file. 
There is thus no reason to read the entire file into memory at once. 
Rather, we can read it line by line, which is much more efficient.
 
We could open the file and assign the result to a variable, but there's no real reason to do that here. 
Instead, we can just invoke open to create the file, and iterate over the lines in it. 
That's because a file object in Python is iterable; we can invoke a for loop over it, 
and thus get its lines, one at a time, without reading the entire file into memory.
 
Notice also that we're wrapping the iteration over the file in enumerate. 
This is often used to provide the indexes of elements in a list over which we're iterating. 
However, we can use it to provide us with the indexes---meaning, the line numbers---as we move over the file. 
Notice that when we use enumerate, we use parallel assignment to get both the index and the line itself.
 
So already, without writing anything in our for loop, we have managed to count 
the number of lines! Note, however, that the number of lines is off by one when you count with "enumerate”.  
One solution is to add 1 to the result -- but we can also invoke enumerate with 
its optional second argument, telling it where to start counting, which is what I have done here.
 
Next, we want to count the number of characters in the file. 
Since we're already iterating over the file, there's not that much work to do:
    We initialize number_of_characters with 0 at the start of the file, 
    and then add to it with each iteration. 
We get the number of characters by calculating len(line), and then adding that 
to number_of_characters with each iteration.
 
Next, we want to count the number of words. In order to get this count, 
we turn line into a list of words, invoking line.split. 
We then count the number of items in the resulting list, 
and add it to our running total of number_of_words.
 
The final item to count is unique words. We could, in theory, 
use a list to store new words. 
But it's much easier to let Python do the hard work for us, 
using a set to guarantee the uniqueness. 
Thus, we create the unique_words set at the start of the program, and then use unique_words.
update to add all of the words in the current line into the set. 
Then, at the end, we merely need to call "len" on our set, 
to find out how many words it contains.
"""


