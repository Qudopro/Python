"""Optional Else clase of a Loop"""

for i in range(2):
    value = int(input('Enter a number (-1 to break): '))
    print("You entered: ", value, end='')

    if(value == -1):
        break

    print()
else:
    print('The loop terminated without executing the break')