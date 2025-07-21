import time

# My intial solution

# Write a for loop that counts to five.

for t in range(1,6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    if t < 6:
        print(f"{t} Mississippi")
    # Body of the loop - use: time.sleep(1)
        time.sleep(1)


# Write a print function with the final message.
print("Ready or not, here I come!")

#Cleaner solution removing the if statement 

# Write a for loop that counts to five.

for t in range(1,6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(f"{t} Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)


# Write a print function with the final message.
print("Ready or not, here I come!")
