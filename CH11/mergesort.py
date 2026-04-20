#mergesort.py
"""Sorting an array with merge sort"""
import numpy as np

#Calls recursive sort_array method to begin merge sorting
def merge_sort(data):
    sort_array(data, 0, len(data) - 1)              #Initiate the recursive algorithm, with 0 and len(data)-1 as the low and high indices of the array to be sorted

#Performs the recursive merge sort algorithm
def sort_array(data, low, high):
    """Split data, sort subarrays and merge them into sorted array"""
    #test base case size of array equals 1. If size = 1, the array is already sorted
    if(high - low) >= 1:                        #If not base case
        #Splits the array in two
        middle1 = (low + high) // 2             #Calculate middle of array (high value of array 1)
        middle2 = middle1 + 1                   #Calculate next element over (low value of array 2)

        #output split step
        print(f'split:   {subarray_string(data, low, high)}')
        print(f'         {subarray_string(data, low, middle1)}')
        print(f'         {subarray_string(data, middle2, high)}')

        #split array in half then sort each half (recursive calls)
        sort_array(data, low, middle1)              #First half of array
        sort_array(data, middle2, high)             #Second half of array

        #Merge two sorted arrays after split calls return
        merge(data, low, middle1, middle2, high)

#Merge two sorted subarrays into one sorted subarray
def merge(data, left, middle1, middle2, right):
    left_index = left           #Index into left (first) subarray.
    right_index = middle2       #Index into right (second) subarray

    combined_index = left       #index into temporary working array
    merged = [0] * len(data)    #Working array

    #output two subarrays before merging
    print(f'merge:   {subarray_string(data, left, middle1)}')
    print(f'         {subarray_string(data,middle2, right)}')

    #Merge arrays until reaching end of either
    while left_index <= middle1 and right_index <= right:
        #Place smaller of two current elements into result and move to next space in arrays
        if data[left_index] <= data[right_index]:               #If the element in the left array is smaller or equal...
            merged[combined_index] = data[left_index]           #Place it in position in the combined array
            combined_index += 1
            left_index += 1
        else:
            merged[combined_index] = data[right_index]
            combined_index += 1
            right_index += 1
    #At the momento... One entire subarray has been placed in the combined array, but the other subarray still contains data


    #If left array is empty (has reached the end)
    if left_index == middle2:           #If true, copy in rest of right array
        merged[combined_index:right+1] = data[right_index:right+1]          #Fill the combined array with the elements of data that represent the right array
    else:                               #Right array is empty, copy in rest of left array
        merged[combined_index:right+1] = data[left_index:middle1+1]         #Fill the combined array with the elements of data that represent the left array

    data[left:right+1] = merged[left:right+1]           #Copy back to data

    #Ouput merged array
    print(f'         {subarray_string(data,left, right)}\n')

#method to output certain values in array
def subarray_string(data, low, high):
    temp = '   ' * low              #Spaces for alignment
    temp += ' '.join(str(item) for item in data[low:high + 1])
    return temp

def main():
    data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
    print(f'Unsorted array: {data}\n')
    merge_sort(data)
    print(f'\nSorted array: {data}\n')

# call main if this file is executed as a script
if __name__ == '__main__':
    main()


