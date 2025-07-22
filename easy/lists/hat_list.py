hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

user_choice = int(input("Choose a number which will replace the middle number from the list:\n"))

hat_list[2] = user_choice

# Step 2: write a line of code that removes the last element from the list.

del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.

length =len(hat_list)

print(length)

print(hat_list)

