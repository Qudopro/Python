"""Find the minimum of three values"""

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

minimum = number1

if minimum > number2:
    minimum = number2
if minimum > number3:
    minimum = number3

print("Minimum value is:\t", minimum)