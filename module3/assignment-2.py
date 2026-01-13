cabin = input(str("Enter the cabin class (LUX, A, B, or C): "))

if cabin == "LUX":
    print(f"Upper-deck cabin with a balcony.")
elif cabin == "A":
    print(f"Above the car deck, equipped with a window.")
elif cabin == "B":
    print(f"Windowless cabin above the car deck.")
elif cabin == "C":
    print(f"Windowless cabin below the car deck.")
else:
    print(f"Invalid cabin class.")