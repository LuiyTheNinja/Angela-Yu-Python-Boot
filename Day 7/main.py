import random
# Inported random for random functions and library.

word_list = ["aardvark", "baboon", "camel"]
# included wordlist with lesson

# =======================================================

# TODO:
# The program should loop and ask the player to guess until they guess wrong 5 times, in which case the man has "hanged"
# Or the program should loop until the player has guessed all the letters in the word, in which case they "win"

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
        print("Right")
    else:
        display += "_"

print(display)