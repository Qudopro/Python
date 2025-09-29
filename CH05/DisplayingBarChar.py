"""Displaying a bar char"""
numbers = [19,3,15,7,11]

print('\nCreating a bar char from numbers')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):
    print(f'{index:>3}\t{value:>8}\t{"*"*value}')