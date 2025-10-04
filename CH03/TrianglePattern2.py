"""Display triange patterns"""

for i in range(1,11):
    for j in range(1,5):
        if j == 1:
            print(f'{'*'*i:<10}', end="   ")
        if(j == 2):
            print(f'{'*'*(11-i):<10}', end="   ")
        if(j == 3):
            print(f'{'*'*(11-i):>10}', end="   ")
        if(j == 4):
            print(f'{'*' * i:>10}', end="   ")
    print()