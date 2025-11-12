"""Calculating Time from seconds"""
"""
Write a script that inputs a number of seconds from the user.
Calculate the number of hours, minutes, and seconds and remaining seconds.
"""
seconds = int(input('Enter the time in seconds: '))

minutes = int(seconds/60)

hours = int(minutes/60)

if hours > 0:
    minutes = minutes%60

if minutes > 0:
    seconds = seconds%60

print(f'The time is {hours:,} hours and {minutes:,} minutes and {seconds:,} seconds')