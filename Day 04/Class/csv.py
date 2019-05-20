import csv

with open('data/passwd') as passwd, open('data/output.csv', 'w') as output:
    r = csv.reader(passwd, delimiter=':')
    w = csv.writer(output, delimiter='\t')
    for record in r:
        if len(record) > 1:
            w.writerow((record[0], record[2]))

 
"""
Discussion
 
The above program uses a number of aspects of Python that are useful when working with files.
 
Here, you can see how with can be used to open two separate files, 
or generally to define any number of objects whose scope is limited to the with block. 
As soon as our block exits, both of the files are automatically closed.
 
We define two variables in the with statement, for the two files  
    The passwd file is opened for reading from /etc/passwd. 
    The output file is opened for writing, to output.csv. 
    Our program will act as a go-between, 
    translating from the input file and placing a reformatted subset into the output file.
 
We do this by creating one instance of csv.reader, which wraps passwd. 
However, because /etc/passwd uses colons (:) to delimit fields, 
we must tell this to csv.reader. 
Otherwise, it will try to use commas, which is almost certainly not going to work well. 
Similarly, we define an instance of csv.writer, wrapping our output file, 
and indicating that we want to use TAB as the delimiter.
 
Now that we have our objects in place for reading and writing CSV data, 
we can run through the input file, writing a row (line) to the output file 
for each of those inputs. 
We take the username (from index 0) and the user ID (from index 2), 
create a tuple, and pass that tuple to csv.writerow. 
Because our csv.writer objects knows how to write to a file, 
and knows what delimiter (TAB) we want to have between the elements, 
it takes care of these automatically.
 
Perhaps the trickiest thing here is to ensure that we do not try to transform lines 
which contain comments---that is, those which begin with a hash (#) character. 
There are a number of ways to do this, but the method that I have employed 
here is simply to check the number of fields we got for the current input line.
If there is only one field, then it must be a comment line, 
or perhaps another type of malformed line. In such a case, we ignore the line.

"""

