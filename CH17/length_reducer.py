#!/usr/bin/env python3
# length_reducer.py
"""Counts the number of words with each length."""
import sys
from itertools import groupby
from operator import itemgetter

#Generator function that reads and splits the k-v pairs produced by the mapper
def tokenize_input():
    """Split each line of standard input into a key and a value."""
    for line in sys.stdin:
        yield line.strip().split('\t')          #Strips any leading or trailing whitespace

# produce key-value pairs of word lengths and counts separated by tabs
for word_length, group in groupby(tokenize_input(), itemgetter(0)):     #Group all word lengths of the same value
    #Call tokenize_input to get the lists representing the k-v pairs
    #Indicates that the k-v pairs should be grouped based on the element at index 0 in each list, that is the key
    try:
        total = sum(int(count) for word_length, count in group)     #totals all the counts for a given key
        print(word_length + '\t' + str(total))          #Outputs a new k-v pair consisting of the word and its total
    except ValueError:
        pass  # ignore word if its count was not an integer