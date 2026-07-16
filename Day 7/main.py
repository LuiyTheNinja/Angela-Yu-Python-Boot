import random
# Imported random for random functions and library.

word_list = ["aardvark", "baboon", "camel"]
# included wordlist with lesson

# =====================================================================

# TODO: Link a wordlist and import above. 
# Maybe add a hangman graphic to the game.

chosen_word = random.choice(word_list)

# For debugging purposes, you can uncomment the following line to see the chosen word.
# print(chosen_word)
# guess = input("Guess a letter: ").lower()

display = ["_"] * len(chosen_word)
counter = 0

print("Current word: " + " ".join(display))

while "".join(display) != chosen_word and counter < 5:
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
    else:
        print("Wrong guess!")
        counter += 1

    print(f"Guesses used: {counter}/5")
    print("Current word: " + " ".join(display))

if "".join(display) == chosen_word:
    print("You win!")
else:
    print("You Lose!")
