inches = float(1)
centimeters = float(0)

while True:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches < 0:
        print("Program ended.")
        break
    elif inches > 0:
        centimeters = inches * 2.54
        print(f"{inches:.1f} inches is {centimeters:.2f} centimeters")