"""Approximating the Mathematical Constant Pi"""
n = 1
while True:
    result = 0
    print("Numero de ciclos: ", n)
    for number in range(0,n):
        value = number*2+1
        if(number % 2 == 0):
            result = result + 4/value
        else:
            result = result - 4/value
    print(result)
    if round(result, 4) == 3.1415:
        break;
    print()
    n += 1
