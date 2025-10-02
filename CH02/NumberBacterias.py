"""Number of bacterias"""
print(f'{"Hour": <20}{"Number of Bacteria":>20}')

for hour in range(0,20,5):
    b = 200*(2**hour)
    print(f'{hour:<20}{b:>20}')