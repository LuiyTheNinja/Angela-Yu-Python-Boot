# Program should print each number from 1 to 100 and include 100.
print(list(range(1, 101)))

# But when the number is devisible by 3, print "Fizz" instead of the number.

for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# When the number is divisible by 5, print "Buzz" instead of the number.

for num in range(1, 101):
    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# And if the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

# Early example result: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

# BONUS: Combine the above into one Function

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0:
            print("Fuzz")
        if num % 5 == 0:
            print("Buzz")
        if num % 3 and num % 5 == 0:
            print("FizzBuzz")
        else:
            print(num)

fizzbuzz()