print("Welcome to the PyPassword Generator!")
num_letters = input("How many letters would you like in your password?")
num_symbols = input("How man symbols would you like in your password?")
num_numbers = input("How many numers would you like in your password?")

letters = ['a', 'b', 'c', 'd', 'e'] # etc all lower and uppcase.
numbers = ['0'] # 0 - 9
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 

# TODO: Add randomization | and Maybe total length(characters?)

final_pass = num_letters + num_symbols + num_numbers
print(f"Your password is {final_pass}")