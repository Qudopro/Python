"""
Write a script that allows the user to input a floating point number, and the number of digits after the decimal sign
"""
number = float(input("Enter a number: "))
decimal = int(input("Enter the number of decimals you wished watch: "))

print(round(number, decimal))
