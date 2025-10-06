import math

def radians(degrees):
    rad = degrees * math.pi / 180
    return rad

degrees = int(input("Enter the degrees between 1 and 180: "))
print(f'Radians =  {radians(degrees):.2f}')
