
while True:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallons < 0:
        print("Program finished.")
        break
    else:
        def gallons_to_liters(liters):
            return 3.785 * liters

        liters = gallons_to_liters(gallons)
        print(f"{gallons:.1f} American gallons is {liters:.2f} liters.")
