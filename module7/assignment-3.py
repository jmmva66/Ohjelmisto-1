from os import name

airports = {}


def add_new_airport():
    icao = input(str("Enter the ICAO code: "))
    name = input(str("Enter the airport name: "))
    airports[icao] = name
    print(f"Airport {name} with ICAO code {icao} has been added.")

def fetch_airports():
    icao = input(str("Enter the ICAO code: "))
    if icao in airports:
        print(f"The airport with ICAO code {icao} is {airports[icao]}.")
    else:
        print(f"No airport found with ICAO code {icao}.")

while True:
    print(f"""\nAirport Data Management
1. Enter a new airport
2. Fetch airport information
3. Quit""")
    userinput = int(input("Please choose an option (1-3): "))
    if userinput == 1:
        add_new_airport()
    elif userinput == 2:
        fetch_airports()
    elif userinput == 3:
        print(f"Thank you for using the Airport Data Management system. Goodbye!")
        break