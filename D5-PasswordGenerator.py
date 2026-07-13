print("Welcome to the PyPassword Generator!")
num_letters = input("How many letters would you like in your password?")
num_symbols = input("How man symbols would you like in your password?")
num_numbers = input("How many numers would you like in your password?")

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# IS there not an import for this?? Surely?? 

# TODO: Generate Pass in Sequence | 
# Then Add randomization | and Maybe total length(characters?)
# Add a Salting Function, and then hashing algorithm. 
# Maybe add a function to tell user, how long it would take to crack their password?

final_pass = num_letters + num_symbols + num_numbers

def pass_standard_check(letters, numbers, symbols, final_pass):
    if letters > 3:
        print("Add more letters!")
    if numbers > 3:
        print("Add more numbers!")
    if symbols > 3:
        print("Add more symbols")
    if len(final_pass) > 12:
        print("Your password does not contain enough characters, \n " \
        "Please select a minium of 12")
    else:
        return(f"Your unscrambled password is {final_pass}")

scramble = input("Would you like to scramble your password for increased security? Y or N")

def scramble_pass():
    if scramble == "Y":
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        # TODO: Scrambling happens here. 


print(f"Your scrambled pass word is {scramble}")