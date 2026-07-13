import random

print("Welcome to the Password Generator!")

num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# There has to be an import for this??


password_chars = []

for _ in range(num_letters):
    password_chars.append(random.choice(letters))

for _ in range(num_symbols):
    password_chars.append(random.choice(symbols))

for _ in range(num_numbers):
    password_chars.append(random.choice(numbers))

unscrambled_password = "".join(password_chars)

def pass_standard_check(letter_count, number_count, symbol_count, password):
    if letter_count < 4:
        print("Consider adding more letters.")

    if number_count < 4:
        print("Consider adding more numbers.")

    if symbol_count < 4:
        print("Consider adding more symbols.")

    if len(password) < 12:
        print("Warning: Password should be at least 12 characters long.")

    print(f"Your unscrambled password is: {password}")

pass_standard_check(
    num_letters,
    num_numbers,
    num_symbols,
    unscrambled_password
)

scramble = input(
    "Would you like to scramble your password for increased security? (Y/N) "
).upper()

if scramble == "Y":
    random.shuffle(password_chars)
    scrambled_password = "".join(password_chars)
    print(f"Your scrambled password is: {scrambled_password}")
else:
    print(f"Your password is: {unscrambled_password}")

#TODO: Add Salting | Add Maximum character limit? | Add Hasing algorithm