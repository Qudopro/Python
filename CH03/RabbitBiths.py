"""Rabbit Births"""
"""
A farmer wants to keep track of the average number of rabbits born on his farm every month.
Develop a sentinel-controlled-repetition script that prompts the suer to input the number of does living in the farm
and the number of rabbits born in a especific month 
"""
total_does = 0
total_baby = 0

does = int(input("Enter the number of does in the rabbit colony (-1 to end):\t"))
while does != -1:
    total_does += does
    baby = int(input('Number of baby rabbits born in the past month:\t'))
    total_baby += baby
    average = baby/does
    print(f'On average {average} baby rabbits wre born for each doe')
    does = int(input("Enter the number of does in the rabbit colony (-1 to end):\t"))

print(f'Total number of baby rabbits for each doe so far: {total_baby/total_does}')