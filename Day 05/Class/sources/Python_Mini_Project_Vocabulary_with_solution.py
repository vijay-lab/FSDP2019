

"""
Code Challenge
  Name: 
    Vocabulary
  Filename: 
    Vocabulary.py
  Problem Statement:
    Novel = james_joyce_ulysses.txt
    The claim is that James Joyce used in his novel more words than any other author. 
    Actually his vocabulary is above and beyond all other authors, 
    maybe even Shakespeare.
    
    1. Find the total number of words in the novel
    2. many words occur multiple time:["the", "while", "good", "bad", "ireland", "irish"]
    3. Quality of a novel is the number of different words.
       Find the number of different words used
    4. look at the other novels and find the total words and unique words for comparison
       novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']

    5. Special Words in Ulysses novel by comparing with others, 
       words which are only used in Ulysses, store it in a file

    6. Common Words - Find the words which occur in every book.

  Hint: 
     Use Sets, Regex, File Handling
     re.findall(r"\b[\w-]+\b", ulysses_txt)
     

"""



"""

The claim is that James Joyce used in his novel more words than any other author. 
Actually his vocabulary is above and beyond all other authors, 
maybe even Shakespeare.

"""


# https://regex101.com/r/cO8lqs/4

import re
# we don't care about case sensitivity and therefore use lower:
ulysses_txt = open("data/james_joyce_ulysses.txt").read().lower()

# \b = Boundary conditions
# \w = [a-zA-Z0-9] alphanumeric characters
# + = occurence more than one
# - = case sensitive
words = re.findall(r"\b[\w-]+\b", ulysses_txt)

print("The novel ulysses contains " + str(len(words)))


# The novel ulysses contains 272452
# This number is the sum of all the words and 
# many words occur multiple time:

for word in ["the", "while", "good", "bad", "ireland", "irish"]:
    print("The word '" + word + "' occurs " + \
          str(words.count(word)) + " times in the novel!" )

# quality of a novel is the number of different words.

# We will turn the list of words "words" into a set. 
# Applying "len" to this set will give us the number of different words:
  
diff_words = set(words)
print("'Ulysses' contains " + str(len(diff_words)) + " different words!")
    
# 'Ulysses' contains 29422 different words!




# look at the other novels in our folder books:
novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis_kafka.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt', 
          'james_joyce_ulysses.txt', 
          'moby_dick_melville.txt']

for novel in novels:
    txt = open("data/" + novel).read().lower()
    words = re.findall(r"\b[\w-]+\b", txt)
    diff_words = set(words)
    n = len(diff_words)
    print("{name:38s}: {n:5d}".format(name=novel[:-4], n=n))



# Special Words in Ulysses
words_in_novel = {}
for novel in novels:
    txt = open("data/" + novel).read().lower()
    words = re.findall(r"\b[\w-]+\b", txt)
    words_in_novel[novel] = words
    
words_only_in_ulysses =  set(words_in_novel['james_joyce_ulysses.txt'])

novels.remove('james_joyce_ulysses.txt')
for novel in novels:
    words_only_in_ulysses -= set(words_in_novel[novel])
    
with open("data/words_only_in_ulysses.txt", "w") as fh:
    txt = " ".join(words_only_in_ulysses)
    fh.write(txt)
    
print(len(words_only_in_ulysses))


# Common Words
# It is also possible to find the words which occur in every book.

# we start with the words in ulysses
common_words = set(words_in_novel['james_joyce_ulysses.txt'])
for novel in novels:
    common_words &= set(words_in_novel[novel])
    
print(len(common_words))



# Doing it Right

"""
We made a slight mistake in the previous calculations. 
If you look at the texts, you will notice that they have a header 
and footer part added by Project Gutenberg, 
which doesn't belong to the texts. 
The texts are positioned between the lines:
    
***START OF THE PROJECT GUTENBERG EBOOK THE WAY OF ALL FLESH***
and
***END OF THE PROJECT GUTENBERG EBOOK THE WAY OF ALL FLESH***
or
*** START OF THIS PROJECT GUTENBERG EBOOK ULYSSES ***
and
*** END OF THIS PROJECT GUTENBERG EBOOK ULYSSES ***
The function read_text takes care of this:
"""


def read_text(fname):
    beg_e = re.compile(r"\*\*\* ?start of (this|the) project gutenberg ebook[^*]*\*\*\*")
    end_e = re.compile(r"\*\*\* ?end of (this|the) project gutenberg ebook[^*]*\*\*\*")
    txt = open("data/" + fname).read().lower()
    beg = beg_e.search(txt).end()
    end = end_e.search(txt).start()
    return txt[beg:end]

words_in_novel = {}
for novel in novels + ['james_joyce_ulysses.txt']:
    txt = read_text(novel)
    words = re.findall(r"\b[\w-]+\b", txt)
    words_in_novel[novel] = words
words_in_ulysses =  set(words_in_novel['james_joyce_ulysses.txt'])

for novel in novels:
    words_in_ulysses -= set(words_in_novel[novel])
    
with open("data/words_in_ulysses.txt", "w") as fh:
    txt = " ".join(words_in_ulysses)
    fh.write(txt)
    
print(len(words_in_ulysses))

    
# we start with the words in ulysses
common_words = set(words_in_novel['james_joyce_ulysses.txt'])
for novel in novels:
    common_words &= set(words_in_novel[novel])
    
print(len(common_words))


# The words of the set "common_words" are words belong to the most 
# frequently used words of the English language.

counter = 0
for word in common_words:
    print(word, end=", ")
    counter += 1
    if counter == 30:
        break


    
    
