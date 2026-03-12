# Create a list of guests
guests = ["Jay-z", "Rakim", "Black Thought"]

# Print an invitation message to each guest
print("Dear " + guests[0] + ", I would like to invite you to dinner.")
print("Dear " + guests[1] + ", I would like to invite you to dinner.")
print("Dear " + guests[2] + ", I would like to invite you to dinner.")

# Original guest list
guests = ["Jay-z", "Rakim", "Black Thought"]

# First set of invitations
print("Dear " + guests[0] + ", I would like to invite you to dinner.")
print("Dear " + guests[1] + ", I would like to invite you to dinner.")
print("Dear " + guests[2] + ", I would like to invite you to dinner.")

# One guest can't make it
print("\nUnfortunately, Rakim can't make it to dinner.")

# Replace the guest who can't attend
guests[1] = "Nas"

# Second set of invitations
print("\nNew invitations:")
print("Dear " + guests[0] + ", I would like to invite you to dinner.")
print("Dear " + guests[1] + ", I would like to invite you to dinner.")
print("Dear " + guests[2] + ", I would like to invite you to dinner.")

# Starting guest list (from Exercise 3-5)
guests = ["Jay-z", "Nas", "Black Thought"]

# Original invitations
print("Dear " + guests[0] + ", I would like to invite you to dinner.")
print("Dear " + guests[1] + ", I would like to invite you to dinner.")
print("Dear " + guests[2] + ", I would like to invite you to dinner.")

# Inform guests about the bigger table
print("\nGood news! I found a bigger dinner table, so I can invite more guests.")

# Add new guests
guests.insert(0, "Beyonce")   # beginning of the list
guests.insert(2, "Michelle Obama")    # middle of the list
guests.append("Cardi B")           # end of the list

# New set of invitations
print("\nNew invitations:")
for guest in guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")


    # Guest list from Exercise 3-6
guests = ["Black Thought", "Jay-z", "Michelle Obama", "Nas", "Beyonce", "Cardi B"]

# Message about shrinking table
print("Unfortunately, the new dinner table won't arrive in time.")
print("I can invite only two people for dinner.\n")

# Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print("Sorry " + removed_guest + ", I can't invite you to dinner.")

# Tell the remaining guests they are still invited
print("\nGuests still invited:")
for guest in guests:
    print("Dear " + guest + ", you are still invited to dinner.")

# Remove the last two guests
del guests[0]
del guests[0]

# Print the final list to confirm it is empty
print("\nFinal guest list:", guests)