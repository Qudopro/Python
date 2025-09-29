"""Using nested control statements to analyze examination results."""

#initialize variables
passes = 0;
failures = 0;

#process 10 students
for student in range(10):
    #get one exam result
    result = int(input("Enter result (1=pass, 2=fail): "))

    if result == 1:
        passes += 1
    else:
        failures += 1


#termination phase
print("Passed: ", passes)
print("Failures: ", failures)

if passes >= 8:
    print("Bonus to instructor")
