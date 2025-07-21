#My first solution

# Prompt the user to enter a word
user_word = input("Enter a word:\n").upper()

# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A":
        continue
    elif letter ==  "E":
        continue 
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)


# Condensed solution 

for letter in user_word:
    if letter in {"A", "E", "I", "O", "U"}:
        continue
    print(letter)


