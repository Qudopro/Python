"""Calculating Time from seconds"""

seconds = int(input('Enter the time in seconds: '))

minutes = int(seconds/60)

hours = int(minutes/60)

if hours > 0:
    minutes = minutes%60

if minutes > 0:
    seconds = seconds%60

print(f'The time is {hours:,} hours and {minutes:,} minutes and {seconds:,} seconds')