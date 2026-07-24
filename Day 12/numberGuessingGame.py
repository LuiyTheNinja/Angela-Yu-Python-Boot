import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Easy should give more attempts than hard
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"\nYou have {attempts} attempt(s) remaining to guess the number.")
    
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess == secret_number:
        print(f" You got it! The answer was {secret_number}.")
        break
    elif guess > secret_number:
        print("Too high!")
        attempts -= 1
    else:
        print("Too low!")
        attempts -= 1

if attempts == 0:
    print(f"\nYou've run out of guesses! The correct number was {secret_number}.")