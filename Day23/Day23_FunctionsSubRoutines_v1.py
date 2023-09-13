#Title: Replit Day  - Day23 - Functions - SubRoutines: The Recipe For Coding - v1


print("----| Replit Login System |-----")
print()


def userAndPass():
    while True:
        userName = "Kev"
        passWord = "pass1"

        yourUserName = input("Username: ")
        yourPassWord = input("Password: ")
        print()

        yourUserName = yourUserName.capitalize()
        print(yourUserName)
        if yourUserName == userName and yourPassWord == passWord:
            print("Correct! Logging in")
            break
        else:
            print("That is incorrect!")
            print("Please try again")
            continue


userAndPass()
