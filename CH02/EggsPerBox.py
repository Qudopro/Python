"""Calculate the number of boxes a farmer needs to store eggs"""
eggs_per_box = 6
number_of_eggs = 29

number_of_boxes = int(number_of_eggs/eggs_per_box)

if(number_of_eggs//eggs_per_box > 0):
    number_of_boxes += 1
    print(f'Eggs placed in the last box: {number_of_eggs//eggs_per_box}')
    print(f'Number of eggs that are needed to fill the last box: {eggs_per_box - number_of_eggs//eggs_per_box}')

print(f'Number of boxes needed: {number_of_boxes}')
