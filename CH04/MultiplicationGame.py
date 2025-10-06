import random as rand

number1 = rand.randint(1, 10)
number2 = rand.randint(1, 10)

multiplication = number1 * number2
status = True
while status:
    print(f'{number1} * {number2} = ')
    dato = int(input("Result of multiplication (-1 to quit): "))

    if dato == -1:
        status = False
    elif(dato == multiplication):
        dato2 = input("You got it!. Do you want to play again? (Y or N)\t\t")
        if(dato2 == "N" or dato2 == "n"):
            status = False
        else:
            number1 = rand.randint(1, 10)
            number2 = rand.randint(1, 10)
            multiplication = number1 * number2
    else:
        print("Wrong input. Goodbye!")
        status = False



