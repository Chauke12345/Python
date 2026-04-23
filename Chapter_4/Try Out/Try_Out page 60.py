# ===============================
# Exercise 4-3: Counting to Twenty
# ===============================
print("4-3: Counting to Twenty")
for number in range(1, 21):
    print(number)
print("\n")  # Blank line for separation

# ===============================
# Exercise 4-4: One Million
# ===============================
print("4-4: One Million (list created, printing commented out)")
numbers = list(range(1, 1000001))
# Printing one million numbers can take a long time
# for number in numbers:
#     print(number)
print("List of 1 to 1,000,000 created.\n")

# ===============================
# Exercise 4-5: Summing a Million
# ===============================
print("4-5: Summing a Million")
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("\n")

# ===============================
# Exercise 4-6: Odd Numbers from 1 to 20
# ===============================
print("4-6: Odd Numbers from 1 to 20")
for number in range(1, 21, 2):
    print(number)
print("\n")

# ===============================
# Exercise 4-7: Threes (Multiples of 3)
# ===============================
print("4-7: Multiples of 3 from 3 to 30")
for number in range(3, 31, 3):
    print(number)
print("\n")

# ===============================
# Exercise 4-8: Cubes of Numbers 1 through 10
# ===============================
print("4-8: Cubes of numbers 1 through 10")
for number in range(1, 11):
    print(number**3)
print("\n")

# ===============================
# Exercise 4-9: Cube Comprehension
# ===============================
print("4-9: Cube Comprehension")
cubes = [number**3 for number in range(1, 11)]
print(cubes)