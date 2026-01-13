import random
diceamount = int(input("How many dice to roll?"))
sumofdice = 0


for i in range(diceamount):
    randomnumber = random.randint(1,6)
    sumofdice +=randomnumber
    print(randomnumber)
print(f"The sum of the dice: {sumofdice}")