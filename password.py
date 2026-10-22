correct="suraj123"
for attempt in range(1,4):
    password=input("enter the password")

    if password == correct:
        break
    else:
        print("Wrong password")

        if attempt==3:
            print("Account Locked")
