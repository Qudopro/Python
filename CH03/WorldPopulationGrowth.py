"""World population Growth"""

population = 8250588863
population_provisional = population
year = 0
print(f'{"Year": <4}{"Population":>30}{"Diferencia":>30}')

for i in range(0,101):
    pop = population
    population = population + population *0.0085

    print(f'{2025+i: < 4}{population:>30,.0f}{pop:>30,.0f}')

    if(population / population_provisional >= 2):
        year = 2025+i
        population_provisional = population

print(f'El ano donde se duplicara la poblacion actual es: {year}')
