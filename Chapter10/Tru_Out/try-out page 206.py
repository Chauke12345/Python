import json

number = input("What is your favorite number? ")

with open("favorite_number.json", "w") as file:
    json.dump(number, file)

    import json

with open("favorite_number.json") as file:
    number = json.load(file)

print(f"I know your favorite number! It's {number}.")

import json

filename = "favorite_number.json"

try:
    with open(filename) as file:
        number = json.load(file)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, "w") as file:
        json.dump(number, file)
    print("I'll remember your favorite number!")
else:
    print(f"I know your favorite number! It's {number}.")

    import json

filename = "user_info.json"

user_info = {
    "username": input("Enter your username: "),
    "age": input("Enter your age: "),
    "favorite_color": input("Enter your favorite color: ")
}

with open(filename, "w") as file:
    json.dump(user_info, file)

# Read it back
with open(filename) as file:
    stored_info = json.load(file)

print("\nHere's what I know about you:")
for key, value in stored_info.items():
    print(f"{key.title()}: {value}")

    import json

filename = "username.json"

def get_stored_username():
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("What is your username? ")
    with open(filename, "w") as file:
        json.dump(username, file)
    return username

def greet_user():
    username = get_stored_username()
    
    if username:
        correct = input(f"Is {username} the correct username? (yes/no): ")
        
        if correct.lower() == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")