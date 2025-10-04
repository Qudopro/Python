"""Rabbit Births"""
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