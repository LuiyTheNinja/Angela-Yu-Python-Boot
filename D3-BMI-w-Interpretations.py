weight = input("what is your weight, in pounds? ")
height = input("what is your height, in inches? ")

# Add function to convert pounds to kilograms and inches to meters, and to convert example 5' 10'' into inches, etc. 

bmi = float(weight) / float(height) ** 2

print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are a normal Weight")
elif 25 <= bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")

