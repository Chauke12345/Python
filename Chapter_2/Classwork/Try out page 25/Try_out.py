# Store the name "Eric" in a variable
name = "Eric"

# Print a greeting message using an f-string
print(f"Hello {name}, would you like to learn some Python today?")

# Store the name again but in lowercase
name = "eric"

# Print the name in all lowercase letters
print(name.lower())

# Print the name in all uppercase letters
print(name.upper())

# Print the name in title case (first letter capitalized)
print(name.title())

# Print a famous quote directly
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# Store the name of the famous person in a variable
famous_person = "Albert Einstein"

# Store the quote in a variable called message
message = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'

# Print the quote stored in the message variable
print(message)


# Store a name with extra whitespace (tabs and new lines)
name = "\t\n  Eric Smith  \n\t"

# Print the original name with whitespace
print("Original name:")
print(name)

# Remove whitespace from the left side of the string
print("Using lstrip():")
print(name.lstrip())

# Remove whitespace from the right side of the string
print("Using rstrip():")
print(name.rstrip())

# Remove whitespace from both sides of the string
print("Using strip():")
print(name.strip())


# Store a filename with a .txt extension
filename = "python_notes.txt"

# Remove the .txt suffix from the filename and print the result
print(filename.removesuffix(".txt"))