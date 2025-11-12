"""Target Heart Rate Calculator"""
"""
Write a script that propts for and inputs the user's age and calculates and display the user's maximum heart rate 
and the range of the user's target heart rate. 
"""
beats_per_minute = 220
age = int(input('Enter your age:\t'))

maximum_heart_rate = beats_per_minute - age

print(f'The maximum heart rate is {maximum_heart_rate}')
print(f'Your target heart rate is minimum {maximum_heart_rate * 0.5}')
print(f'Your target heart rate is maximum {maximum_heart_rate * 0.85}')

beats = int(input('Enter the number of your beats:\t'))
if beats >= maximum_heart_rate*0.5 and beats <= maximum_heart_rate*0.85:
    print('It is all right')
else:
    print('It is not right')