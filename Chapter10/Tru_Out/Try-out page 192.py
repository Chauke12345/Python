name = input("What is your name? ")

with open("guest.txt", "w") as file:
    file.write(name)

print("Your name has been written to guest.txt.")

with open("guest_book.txt", "a") as file:
    while True:
        name = input("Enter your name (or type 'quit' to exit): ")
        
        if name.lower() == "quit":
            break
        
        file.write(name + "\n")
        print(f"Hello, {name}! You've been added to the guest book.")