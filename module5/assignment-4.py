Cities = []
cityamount = 5


for i in range(cityamount):
    City = str(input("Enter the name of a city: "))
    Cities.append(City)


print("\n\nThe cities you entered: ")
for city in Cities:
    print(city)