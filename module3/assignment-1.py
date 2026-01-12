zander_size = float(input("Enter the length of the zander in centimeters: "))

zander_lacking_size = 0

if zander_size < 42:
    zander_lacking_size = 42 - zander_size
    print (f"The zander does not meet the size limit.\nPlease release the fish back into the lake.\nThe fish was {zander_lacking_size:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")
