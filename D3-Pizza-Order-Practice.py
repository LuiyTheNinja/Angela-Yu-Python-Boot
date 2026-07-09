# Day 3: Pizza Order Practice Challenge

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
total = 0

if size == 'S':
    total += 15
if size == 'M':
    total += 20
if size == 'L':
    total += 25

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3
else:
    total += 0

if cheese == "Y":
    total += 1
else:
    total += 0

print(f"Your total is ${total}!")
