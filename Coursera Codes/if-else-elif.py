def hint_username(usernme):
    if len(usernme) < 3:
        print("Invalid Username!")
    elif len(usernme)>15:
        print("Invalid Username")
    else:
        print("Valid Username")


hint_username(str(input("Enter the username: ")))