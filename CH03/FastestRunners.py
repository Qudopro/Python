"""Fastest Runner"""
"""
Use a loop to find the fastest and second fastest from 10 runners whose speeds are entered
"""
import random as rnd
maximum = 0
maximum2 = 0
maximum3 = 0

for i in range(1,4):
    number = int(input('Enter a number: '))
    #ENCUENTRA EL VALOR MAS GRANDE
    if maximum < number :                           #maximum = 7                   8                9
        maximum = number

    if i == 1:
        maximum3 = maximum                          #maximum3 = 7                   False           False
        continue
    else:
        if maximum3 < maximum:
            maximum2 = maximum3                     #                               7
        else:
            if maximum2 < number:                   #
                maximum2 = number                   #

        maximum3 = maximum;                         #



print(f'El corredor mas rapido tuvo una velocidad de: {maximum}m/s')
print(f'El segundo corredor mas rapido tuvo una velocidad de: {maximum2}m/s')
