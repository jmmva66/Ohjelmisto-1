smallestnumber = None
largestnumber = None

while True:
    inputnumber = input("Enter a number (or press Enter to quit): ")
    if inputnumber == "":
        print(f"Smallest number: {smallestnumber:.1f}\nLargest number: {largestnumber:.1f}")
        break
    else:
        inputnumber = int(inputnumber)
        if smallestnumber is None:
            smallestnumber = inputnumber
        elif inputnumber < smallestnumber:
            smallestnumber = inputnumber

        if largestnumber is None:
            largestnumber = inputnumber
        elif inputnumber > largestnumber:
            largestnumber = inputnumber