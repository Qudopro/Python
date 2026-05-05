#selectionsortanimation.py
"""Animated selection sort visualization"""
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import seaborn as sns
import sys
from soundutilities import play_sound

#Redraw the animation's graphical elements
def update(frame_data):
    """Display bars representing the current state"""
    #unpack info for graph update
    data, colors, swaps, comparisons = frame_data
    #data = the array being sorted
    #colors = array of color names containing the specific color for each bar
    #swaps = integer representing the number of swaps performed so far
    #comparisons = an integer representing the number of comparisons performed so far
    plt.cla()           #Clear old contents of current Figure

    #create barplot and set its xlabel
    bar_positions = np.arange(len(data))
    axes = sns.barplot(bar_positions, data, palette=colors)         #new bars with specific colors
    axes.set(xlabel=f'Comparisons: {comparisons}; Swaps: {swaps}', xticklabels=data)

def flash_bars(index1, index2, data, colors, swaps, comparisons):
    """Flash the bars about to be swapped and play their notes"""
    for x in range(0,2):
        #Creación de efecto de flash en el grafico
        colors[index1], colors[index2] = 'white', 'white'                   #Borra las barras al dibujarlas en blanco
        yield(data, colors, swaps, comparisons)                         #FunctAnimation uses the values to pass them to funciton update and drawing the next animation
        colors[index1], colors[index2] = 'purple', 'purple'             #Appear the bars in purple color
        yield(data, colors, swaps, comparisons)
        #Reproduce por 0.05 segundos la nota de frecuencia correspondiente a la magnitud de la barra
        play_sound(data[index1], second=0.05)
        play_sound(data[index2], second=0.05)

def selection_sort(data):
    """Sort data using the selection sort algorithm and yields values that update uses to visualize the algorithm"""
    swaps = 0
    comparisons = 0
    colors = ['lightgray'] * len(data)          #List of bar colors. All the bars should be 'lighgray' initially

    #Display initial bars representing shuffled values
    yield(data, colors, swaps, comparisons)                 #Yield values to the FuncAnimation to pass to the update function. Unsorted order

    #loop over len(data) - 1 elements. Implements the selection sort algorithm
    for index1 in range(0, len(data) - 1):
        smallest = index1

        # loop to find index of smallest element's index
        for index2 in range(index1 + 1, len(data)):
            comparisons += 1                            #Track of the total number of comparisons performed
            colors[smallest] = 'purple'
            colors[index2] = 'red'                      #Represents the value currently being compared with the smallest value during the current pass
            yield(data, colors, swaps, comparisons)     #Yield values indicating the values that are being compared
            play_sound(data[index2], second=0.05)       #Play a musical note corresponding to the red's magnitude

            #Compare elements at positions index and smalles. It ensures that only one bar is red and one is purple during the compariosns
            if data[index2] < data[smallest]:
                colors[smallest] = 'lightgray'
                smallest = index2
                colors[smallest] = 'purple'
                yield(data, colors, swaps, comparisons)
            else:
                colors[index2] = 'lightgray'
                yield(data, colors, swaps, comparisons)

        #ensure that last bar is not purple at the end of a pass
        colors[-1] = 'lightgray'

        #Flash the bars about to be swapped
        yield from flash_bars(index1, smallest, data, colors, swaps, comparisons)           #Chained generator functions. Call the latter function in a yield from statement
        #The values yielded by flash_bars pass through to the FuncAnimation for the next update call

        #Swap the elements at positions index1 and smallest
        swaps += 1                                                  #Increment the swaps counted
        data[smallest], data[index1] = data[index1], data[smallest] #Perform the swap

        #flash the bars that were just swapped
        yield from flash_bars(index1, smallest, data, colors, swaps, comparisons)

        #Indicate that bar index1 is now in its final spot
        colors[index1] = 'lightgreen'
        yield(data, colors, swaps, comparisons)

    #Indicate that last bar is now in its final spot
    colors[-1] = 'lightgreen'
    yield(data, colors, swaps, comparisons)
    play_sound(data[-1], seconds=0.05)

    #Play each bar's note once and color it darker green
    for index in range(len(data)):
        colors[index] = 'green'
        yield(data, colors, swaps, comparisons)
        play_sound(data[index], second=0.05)

    #FuncAnimation terminates because of selection_sort function terminates

def main():
    number_of_values = int(sys.argv[1]) if len(sys.argv) == 2 else 10

    figure = plt.figure('Selection Sort')           #Figure to display barplot
    numbers = np.arange(1, number_of_values + 1)        #Create array
    np.random.shuffle(numbers)          #Shuffle the array

    #start the animation
    anim = animation.FuncAnimation(figure, update, repeat=False, frames=selection_sort(numbers), interval=50)

    plt.show()          #Display the Figure

#call main if this file is executed as a script
if __name__ == '__main__':
    main()
