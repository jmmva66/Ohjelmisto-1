number = int(input("Enter an integer: "))

divider = 0

while divider <= number:
    print(f"dividing {number} by {divider}")
    if number % divider == 0:
        print(f"{number} is not a prime number")
        break
    else:
        print(f"{number} is a prime number")