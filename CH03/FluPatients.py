"""Keep track of the number of infected patients"""
total = 0
minimum = 0
maximum = 0
for day in range(1,7):
    number_of_infected_patients = int(input(f'How many infected patients do you have in day: {day}?\t'))
    if day == 1:
        minimum = number_of_infected_patients
    if minimum > number_of_infected_patients:
        minimum = number_of_infected_patients
    if maximum < number_of_infected_patients:
        maximum = number_of_infected_patients
    total += number_of_infected_patients



print(f"\n\nTotal number of infected patients: {total}")
print(f'Average number of infected patients per day: {(total/7):.2f}')
print(f'Minimum number of infected patients per day: {minimum}')
print(f"Maximum number of infected patients per day: {maximum}")
