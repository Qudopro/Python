"""Simulating the dice game Craps."""
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple"""
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    return (dice1, dice2)       # Pack dice face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice"""
    dice1, dice2 = dice         # Unpack the tuple into variables
    print(f'Player rolled {dice1} + {dice2} = {sum(dice)}')

dice_values = roll_dice()
display_dice(dice_values)

#Determine game status and point, based on first roll
sum_of_dice = sum(dice_values)

if sum_of_dice in (7, 11):
    game_status = "WON"
elif sum_of_dice in(2,3,12):
    game_status = "LOST"
else:
    game_status = "CONTINUE"
    my_point = sum_of_dice
    print("Point is:", my_point)

#Continue rolling until player wins or loses
while game_status == "CONTINUE":
    dice_values = roll_dice()
    display_dice(dice_values)
    sum_of_dice = sum(dice_values)

    if sum_of_dice == my_point:
        game_status = "WON"
    elif sum_of_dice == 7:
        game_status = "LOST"

#Display wins or loses message
if game_status == "WON":
    print("Player wins!")
else:
    print("Player loses!")