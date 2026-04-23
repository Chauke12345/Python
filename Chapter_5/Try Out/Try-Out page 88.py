usernames = ["admin", "Hleko", "Rimitso", "Hletelo", "Simeko"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

        usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

    current_users = ["Admin", "Hleko", "Rimitso", "Hletelo", "Simeko"]
new_users = ["Eddie", "Sue", "EMELY", "mandla", "Sbu"]

# make lowercase copy
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' is already taken. Please choose another.")
    else:
        print(f"The username '{user}' is available.")

        numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")