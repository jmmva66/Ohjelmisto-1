import random

#numerot ensimmäiseen koodiin
d1 = random.randint(0,9)
d2 = random.randint(0,9)
d3 = random.randint(0,9)

#numerot toiseen koodiin
d4 = random.randint(1,6)
d5 = random.randint(1,6)
d6 = random.randint(1,6)
d7 = random.randint(1,6)


first_code = (f"{d1}{d2}{d3}")

second_code = (f"{d4}{d5}{d6}{d7}")

print("3-digit code:", (first_code))
print("4-digit code:", (second_code))