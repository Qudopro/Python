#!/usr/bin/env python3
# length_mapper.py
"""Maps lines of text to key-value pairs of word lengths and 1."""
import sys

def tokenize_input():
    """Split each line of standard input into a list of strings."""
    for line in sys.stdin:                  #Reads lines of text from the standard input stream and for each returns a list of strings
        yield line.split()

# read each line in the the standard input and for every word  produce a key-value pair containing the word, a tab and 1
for line in tokenize_input():           #Iterate through the lists of strings from tokenize_input
    for word in line:                   #For every word in that list
        print(str(len(word)) + '\t1')           #Outputs a key-value pair with the word's length as the key, a tab, and the value 1, indicating that there's one word of that length

#MapReduce algorithm's reduction step will summarize these key-value pairs reducing all those with the same key to a single key-value pair with the total count
