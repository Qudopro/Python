"""Summarizes grades of student"""

x = int(input("Enter the grades of course 1:\t"))
y = int(input("Enter the grades of course 2:\t"))
z = int(input("Enter the grades of course 3:\t"))

average = (x+y+z)/3

print(f'The average of the student is: {average}')

min = x
if min > y:
    min = y
if min > z:
    min = z

max = x
if max < y:
    max = y
if max < z:
    max = z

print(f'The lowest grade is {min}')
print(f'The highest grade is {max}')