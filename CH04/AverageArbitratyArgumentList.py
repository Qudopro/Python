"""Average of an arbitrary argument list"""

def average(*args):
    return sum(args) / len(args)


print(average(3,4,5,6,7,8))
