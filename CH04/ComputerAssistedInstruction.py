"""Computer-assisted instruction (CAI). Learn multiplication!"""
import random as rand

def message_possitive():
    number_message = rand.randint(1,3)
    if number_message == 1:
        return "Very good!"
    elif number_message == 2:
        return "Nice work!"
    else:
        return "Keep up good work!"

def message_incorrect():
    number_message = rand.randint(1,3)
    if number_message == 1:
        return "No. Please try again!"
    elif number_message == 2:
        return "Wrong. Try once more"
    else:
        return "No. Keep trying"

def generate_numbers():
    return (rand.randint(1, 10), rand.randint(1, 10))


def generate_numbers2():
    return (rand.randint(11, 99), rand.randint(11, 99))

status = True
status_difficulty = True
status_game = True
option = 0
while status_game:
    print("Welcome to Computer Assisted Instructions!")
    print("Select your game: ")
    print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Random")
    option = int(input())

    if option >= 1 and option <= 5:
        status_game = False
    else:
        print("Try again")


if option == 5:
    option = rand.randint(1,4)

while status_difficulty:
    difficulty = int(input("Select your difficult!\t\t"))
    if difficulty == 1:
        number1, number2 = generate_numbers()
        status_difficulty = False
    elif difficulty == 2:
        number1, number2 = generate_numbers2()
        status_difficulty = False
    else:
        print("Try again!")

if option == 1:
    while status:
        addition = number1 + number2
        print(f'How much is {number1} + {number2} ?\t')
        data = int(input())
        if data == addition:
            print(message_possitive())
            dato2 = input('Do you want to do another addition? (Y or N):\t')
            if (dato2 == "N" or dato2 == "n"):
                status = False
        else:
            print(message_incorrect())
            continue
        number1, number2 = generate_numbers()
elif option == 2:
    while status:
        subtraction = number1 - number2
        print(f'How much is {number1} - {number2} ?\t')
        data = int(input())
        if data == subtraction:
            print(message_possitive())
            dato2 = input('Do you want to do another subtraction? (Y or N):\t')
            if (dato2 == "N" or dato2 == "n"):
                status = False
        else:
            print(message_incorrect())
            continue
        number1, number2 = generate_numbers()
elif option == 3:
    while status:
        multiplication = number1 * number2
        print(f'How much is {number1} times {number2} ?\t')
        data = int(input())
        if data == multiplication:
            print(message_possitive())
            dato2 = input('Do you want to do another multiplication? (Y or N):\t')
            if(dato2 == "N" or dato2 == "n"):
                status = False
        else:
            print(message_incorrect())
            continue
        number1, number2 = generate_numbers()
elif option == 4:
    while status:
        division = number1 / number2
        print(f'How much is {number1} / {number2} ?\t')
        data = int(input())
        if data == division:
            print(message_possitive())
            dato2 = input('Do you want to do another division? (Y or N):\t')
            if(dato2 == "N" or dato2 == "n"):
                status = False
        else:
            print(message_incorrect())
            continue
        number1, number2 = generate_numbers()