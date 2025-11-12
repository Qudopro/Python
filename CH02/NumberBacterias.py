"""Number of bacterias"""
"""
Starting with 200 bacteria, the growth in the number of bacteria after n hours is calculated as B = 200x 2^n.
Print the number of bacteria after 0, 5, 10, 15 hours in table format. 
"""
print(f'{"Hour": <20}{"Number of Bacteria":>20}')

for hour in range(0,20,5):
    b = 200*(2**hour)
    print(f'{hour:<20}{b:>20}')