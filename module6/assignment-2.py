import random

roll = 1
amount_of_sides = int(input("How many sides would you like to have? "))

def roll_dice(amount_of_sides):
    while True:
        roll = int(random.randint(1, amount_of_sides))
        return roll

while roll != amount_of_sides:
    roll = roll_dice(amount_of_sides)
    print(roll)