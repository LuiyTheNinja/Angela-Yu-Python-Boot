# Day 2 Project: Tip Calculator

bill_total = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15, or 20? "))
num_people = int(input("How many people to split the bill? "))

tip_amount = bill_total * (tip_percentage / 100)
total_bill = bill_total + tip_amount
bill_per_person = total_bill / num_people

print(f"Each person should pay: ${bill_per_person:.2f}")