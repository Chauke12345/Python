while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break
    
    print(f"I'll add {topping} to your pizza.")

while True:
    age = input("Enter your age (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a topping (or 'quit' to stop): ")
    
    if topping.lower() != 'quit':
        print(f"I'll add {topping} to your pizza.")

active = True

while active:
    topping = input("Enter a topping (or 'quit' to stop): ")
    
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

while True:
    topping = input("Enter a topping (or 'quit' to stop): ")
    
    if topping.lower() == 'quit':
        break
    
    print(f"I'll add {topping} to your pizza.")

while True:
    print("This loop will run forever!")