import random

roll = 1

def roll_dice():
    while True:
        roll = int(random.randint(1, 6))
        return roll

while roll != 6:
    roll = roll_dice()
    print(roll)