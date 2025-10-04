"""A user inputs a position (a number) and the number in that position in the Fibonacci sequence is displayed."""
def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

x = int(input("Enter a Fibonacci number: "))
print(f'The number of fibonacci is: {fibonacci(x)}')




