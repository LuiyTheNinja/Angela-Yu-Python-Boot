# Day 3: Pizza Order Practice Challenge

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

if size == 'S':
    size += 15
if size == 'M':
    size += 20
if size == 'L':
    size += 25

if pepperoni == "Y":
    if size == "S":
        pepperoni += 2
    else:
        pepperoni += 3
else:
    pepperoni == 0

if cheese == "Y":
    cheese += 1
else:
    cheese == 0

total = size + pepperoni + cheese
print(f"Your total is ${total}!")
