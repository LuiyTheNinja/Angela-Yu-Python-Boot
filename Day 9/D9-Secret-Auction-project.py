import art

print(art.logo)


# TODO-1: Ask the user for input = DONE
# TODO-2: Save data into dictionary {name: price} = DONE
# TODO-3: Whether if new bids need to be added - Does this mean, the bids should only hold onto the largest bid? or should it hold onto all the bids? 
# TODO-4: Compare bids in dictionary 


print("Welcome to the secret auction program.")
should_continue = input("Do you want to make a bid? Type 'yes' or 'no': ")

while should_continue == "yes":
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids = {name: bid} # how to add new bids to the dictionary without overwriting the previous ones?
  should_continue = input("Is there another Bidder? Type 'yes' or 'no': ")

print(bids)


