talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

kilograms =0

total_grams = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3

remaining_grams: float = total_grams
while remaining_grams >= 1000:
    remaining_grams -= 1000
    kilograms +=1


print (f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")
