#binarysearch.py
"""Use a binary search to locate an item in an array"""
import numpy as np

def binary_search(data, key):
    """Perform binary search of data looking for key"""
    low = 0                 #Low end of search area
    high = len(data) - 1    #High end of search area
    middle = (high + low + 1) // 2              #Middle element index. The average of low and high
    location = -1           #Return value -1 if not found

    #loop to search for element
    while low <= high and location == -1:
        # print remaining elements of array
        print(remaining_elements(data, low, high))

        print('   ' * middle, end='')           #output spaces for alignment
        print(' * ')                            #Indicate current middle

        #if element is found at the middle
        if key == data[middle]:
            location = middle                   #location is the current middle
        elif key < data[middle]:                #middle element is too high
            high = middle - 1                   #eliminate the higher half
        else:                                   #middle element is too low
            low = middle + 1                    #eliminate the lower half

        middle = (high + low + 1) // 2          #Recalculate the middle
    return location

def remaining_elements(data, low, high):
        """Display remaining elements of the binary search"""
        return '   ' * low + ' '.join(str(s) for s in data[low:high + 1])

def main():
    #create and display array of random values
    data = np.random.randint(10,91,15)
    data.sort()
    print(data, '\n')

    search_key = int(input('Enter key to search or -1 to quit: '))

    #repeatedly input an integer; -1 terminates the program
    while search_key != -1:
        location = binary_search(data, search_key)          #perform search

        if location == -1:              #not found
            print(f'{search_key} not found\n')
        else:
            print(f'{search_key} found in position {location}\n')

        search_key = int(input('Enter key to search or -1 to quit: '))

if __name__ == '__main__':
    main()

