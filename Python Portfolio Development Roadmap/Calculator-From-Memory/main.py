print("Welcome to Simple Calculator")
input_choice = input("Select operation: 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division: ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if input_choice == "1":
    print("You selected operation: Addition")
elif input_choice == "2":
    print("You selected operation: Subtraction")
elif input_choice == "3":
    print("You selected operation: Multiplication")
elif input_choice == "4":
    print("You selected operation: Division")


if input_choice == '1':
    print(number1 + number2)
elif input_choice == '2':
    print(number1 - number2)
elif input_choice == '3':
    print(number1 * number2)
elif input_choice == '4':
    print(number1 / number2)
else:
    print("Invalid input")