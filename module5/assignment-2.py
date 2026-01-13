numberlist = []

userinput = (input("Enter a number: "))
while userinput!="":

    numberlist.append(float(userinput))
    userinput = (input("Enter a number: "))

print("The greatest numbers in descending order: ")
numberlist.sort(reverse=True)

for i in numberlist[:5]:
    print(i)