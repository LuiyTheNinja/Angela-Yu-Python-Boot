import random

number_list = list(range(101))

secret_number = random.choice(number_list)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

guess = input("Make a guess!: ")

while guess != secret_number:
  if difficulty == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
    guess = input("Make a guess!")
if difficulty == 'hard':
    print("You have 4 attemps remaining to guess the number.")
    attempts = 4
    guess = input("Make a guess!")

