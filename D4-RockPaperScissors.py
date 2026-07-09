import random
# Python uses the Mersenne Twister. 
# we use the import random for this. 
# in the documentation for this, we can all the things this does. 
# here we will use randint. 

# random_integer = random.randint(1 , 10)
# print(random_integer)

# We can also split code up into individual modules, which is what is done above. 
# to import into another py file. We do
# "import filename"
# to then call specific functions or variables, we need to use full stop with the file name
# ex: print(my_module.my_favourite_number)
# random.random() will generate a foat between 0 and 1. 
# We can multiple the random.random to increase the random range.
# ex: random.random() * 10 will give us floats between 0 and 10. 

# random.uniform(a, b) will generate numbers between and inclusie of a and b. Favors upper bound
# preferable to use random.random() * <whatever number is needed>

# ==================================================================

# Code for Player input

user_input = input("What do you choose? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors.\n")

# Temporary code to display the user's choice
if user_input == "0":
    print("You chose Rock.")
elif user_input == "1":
    print("You chose Paper.")
else:
    print("You chose Scissors.")
# =========================================

# Function to generate a random computer choice. 
computer_choice = random.randint(0, 2)

def computer_choice():
    if computer_choice == 0:
        print("Computer chose Rock!")
    elif computer_choice == 1:
        print("Computer chose Paper!")
    else: 
        print("Computer chose Scissors!")

# ==============================================

# TODO: Include ASCI Art for player and computer choices. | Determine winner 

def result():
    if user_input == 0 and computer_choice == 0 or user_input == 1 and computer_choice == 1 or user_input == 2 and computer_choice == 2:
        print("Tie! Try Again!")
    if user_input == 1 and computer_choice == 1:
        print("Computer wins!")

