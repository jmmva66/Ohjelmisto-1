

def get_season(month_number):
    season = str(month_number)
    if month_number == 12 or month_number <=2:
        return "winter"
    elif month_number <= 5:
        return "spring"
    elif month_number <= 8:
        return "summer"
    elif month_number <= 11:
        return "autumn"
    return season

while True:
    userinput = int(input("Enter the number of a month (1-12): "))
    print(f"You entered: {userinput}")
    if userinput < 1 or userinput > 12:
        print("Please enter a number between 1 and 12.")
        break
    else:
        season = get_season(userinput)
        print(f"The season is {season}.")
        break