"""Using nested control statements to analyze examination results"""

#Initialize variables
passes = 0          #Number of passes
fails = 0           #Number of failures

#Process 10 students
for student in range(10):
    #Get one exam result
    result  = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes += 1
    else:
        fails += 1

#Termination phase
print('Total passes:', passes)
print('Total fails:', fails)

if passes > 8:
    print('Bonus to instructor')