sex = str(input("Enter biological gender (male/female): "))
sex = sex.lower()

hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if sex != "male" and sex != "female":
    print("Invalid gender.")
else:
    if sex == "male":
        if hemoglobin < 134:
            print("Your hemoglobin is low.")
        elif hemoglobin > 167:
            print("Your hemoglobin is high.")
        else:
            print("Your hemoglobin is normal.")
    elif sex == "female":
        if hemoglobin < 117:
            print("Your hemoglobin is low.")
        elif hemoglobin > 155:
            print("Your hemoglobin is high.")
        else:
            print("Your hemoglobin is normal.")