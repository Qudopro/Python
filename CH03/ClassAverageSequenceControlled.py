"""Class Average program with sequence-controlled repetition"""

#Initialization phase
total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79,82,94] #List of integers

#Processing phase
for grade in grades:
    total += grade
    grade_counter += 1

#Termination phase
average = total / grade_counter
print(f"Class average is {average}")