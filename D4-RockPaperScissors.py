import random

# ASCII Art representations for the choices
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# ==================================================================
# Player Input
# ==================================================================
user_input = input("What do you choose? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors.\n")

# Convert input to integer for logic comparison, default to -1 if invalid
if user_input in ["0", "1", "2"]:
    player_choice = int(user_input)
else:
    player_choice = -1

# Display player choice and art
print("\n--- YOUR CHOICE ---")
if player_choice == 0:
    print("You chose Rock.")
    print(rock_art)
elif player_choice == 1:
    print("You chose Paper.")
    print(paper_art)
elif player_choice == 2:
    print("You chose Scissors.")
    print(scissors_art)
else:
    print("Invalid choice!")

# ==================================================================
# Computer Choice
# ==================================================================
# Only have the computer play if the player made a valid move
if player_choice != -1:
    computer_choice = random.randint(0, 2)

    print("--- COMPUTER CHOICE ---")
    if computer_choice == 0:
        print("Computer chose Rock!")
        print(rock_art)
    elif computer_choice == 1:
        print("Computer chose Paper!")
        print(paper_art)
    else: 
        print("Computer chose Scissors!")
        print(scissors_art)

# ==================================================================
# Determine Winner
# ==================================================================
print("--- RESULT ---")
if player_choice == -1:
    print("You lose by default for picking an invalid option.")
elif player_choice == computer_choice:
    print("Tie! Try Again!")
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win! 🎉")
else:
    print("Computer wins! 🤖")