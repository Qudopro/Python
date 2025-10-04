"""Display triange patterns"""
#Figure 1
for i in range(1,11):
    print("*"*i, end="\n")

print("\n\n")

#Figure 2
for i in range(10,0,-1):
    print("*"*i, end="\n")

print("\n\n")


#Figure 3
for i in range(1,11):
    print(f'{"*"*i:>10}')
print("\n\n")
#Figure 4
for i in range(10,0,-1):
    print(f'{"*"*i:>10}')

