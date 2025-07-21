word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word:\n").upper()


for letter in user_word:
    if letter in {"A", "E", "I", "O", "U"}:
        continue
    else:
        word_without_vowels += letter

# Print the word assigned to word_without_vowels.

print(word_without_vowels)


# Imporvemnt, simply remove the else 

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word:\n").upper()


for letter in user_word:
    if letter in {"A", "E", "I", "O", "U"}:
        continue
    word_without_vowels += letter

# Print the word assigned to word_without_vowels.

print(word_without_vowels)