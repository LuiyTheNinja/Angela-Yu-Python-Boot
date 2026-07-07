weight = input("what is your weight, in pounds? ")
height = input("what is your height, in inches? ")

# Add function to convert pounds to kilograms and inches to meters, and to convert example 5' 10'' into inches, etc. 

bmi = float(weight) / float(height) ** 2

print(f"Your BMI is {bmi}")