"""Calculate the mean, median and mode of the temperatures measured in Sidney on the first 10 days of February"""
import statistics

temperatures = [19.5, 19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2, 19.5, 20.2]

print(f'Temperatures: {temperatures}')

print(f'Mean: {statistics.mean(temperatures)}')
print(f'Mode: {statistics.mode(temperatures)}')
print(f'Median: {statistics.median(temperatures)}')
