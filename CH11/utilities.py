#utilities.py
"""Utility function for printing a pass of the insertion_sort and selection_sort algorithms"""

def print_pass(data, pass_number, index):
    """Print a pass of the algorithm"""
    label = f'After pass {pass_number}: '
    print(label, end='')

    #output elements up to selected item
    print('  '.join(str(d) for d in data[:index]), end='  ' if index != 0 else '')          #Elements from the beginining of the array p to position index, separated by two spaces each

    print(f'{data[index]}*  ', end='')       #Indicate swap with *

    #output rest of elements
    print('  '.join(str(d) for d in data[index + 1:len(data)]))         #Print the rest of the array's elements

    #Underline elements that are sorted after this pass_number
    print(f'{" "*len(label)}{"--  "*pass_number}')                  #Display dashes under the sorted portion of the array