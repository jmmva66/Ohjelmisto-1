names = set()

while True:
    userinput = input("Enter name")
    if userinput in names:
        print("Existing name")
    elif userinput != "":
        names.add(userinput)
        print("New name")
    if userinput == "":
        print(names)
        break