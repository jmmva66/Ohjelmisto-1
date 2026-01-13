Username = str("python")
password = str("rules")
attemptsleft = int(5)

while attemptsleft > 0:
    enterusername = input("Enter username: ")
    enterpassword = input("Enter password: ")
    if enterusername == Username and enterpassword == password:
        print("Welcome")
        break
    else:
        attemptsleft -= 1
        if attemptsleft == 0:
            print("Access denied")
            break
        else:
            print("Incorrect username or password. Please try again.")