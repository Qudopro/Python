#insertionsort.py
""""Sorting an array with insertion sort"""
import numpy as np
from utilities import print_pass

def insertion_sort(data):
    """Sort an array using insertion sort"""
    #loop over 1 up to len(data) elements
    for next in range(1, len(data)):
        #Selecciona el elemento y el índice que deseas mover
        insert = data[next]                 #Value to insert
        move_item = next                    #Location to place element

        #Search for place to put current element
        while move_item > 0 and data[move_item-1] > insert:             #Mientras no se llegue al inicio del arreglo o cuando el valor a la izquierda del elemento sea mayor al elemento que se busca insertar
            data[move_item] = data[move_item-1]         #Recorre el elemento anterior a la derecha del que se busca insertar
            move_item -= 1                              #Decrementa el índice del elemento que se busca insertar en uno

        data[move_item] = insert                        #Coloca el elemento que se buscaba mover en el índice apropiado
        print_pass(data, next, move_item)               #Output pass of algorithm

def main():
    data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
    print(f'Unsorted array: {data}\n')
    insertion_sort(data)
    print(f'\nSorted array: {data}\n')

# call main if this file is executed as a script
if __name__ == '__main__':
    main()


