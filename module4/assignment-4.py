import random

randomnumber = random.randint(1,10)
print(f"the random number is {randomnumber}")

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == randomnumber:
        print("Correct")
        break
    elif guess > randomnumber:
        print("Too high")
    elif guess < randomnumber:
        print("Too low")