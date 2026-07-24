📝 Part 1: Python Study Notes (Extracted)🎲 Random ModuleMersenne Twister: Python uses the Mersenne Twister algorithm as its core generator for the random module.random.randint(a, b): Generates a random integer between $a$ and $b$ (inclusive).random.random(): Generates a random float between 0.0 and 1.0 (exclusive of 1.0).Tip: Multiply the result to increase the range (e.g., random.random() \* 10 yields floats between 0 and 10).random.uniform(a, b): Generates a floating-point number between $a$ and $b$ (inclusive/favors upper bound depending on rounding).📦 Code ModularizationTo split code up into individual files and use them elsewhere:Pythonimport filename # Do not include the .py extension

# Call specific functions or variables using dot notation:

print(filename.my_favourite_number)
📋 Working with ListsPython# Initialization and Modification
my_list = ["item1", "item2"]
my_list[1] = "item3" # Replaces "item2" with "item3" (Index 1)

# Adding Items

my_list.append("item4") # Adds a single item to the end
my_list.extend(["item5", "item6"]) # Adds multiple items to the end

# Index & "Off-by-One" Errors

# If a list has 50 items, len(list) is 50, but the maximum index is 49.

# incorrect: print(my_list[len(my_list)]) -> Throws IndexError

# correct: print(my_list[len(my_list) - 1])

# Nested Lists (Lists within Lists)

fruits = ['apple', 'banana']
vegetables = ['spinach']
dirty_dozen = [fruits, vegetables]

# for loop in Python lists.

for item in list_of_items:

# sum() allows input of any iterable data type including lists.

# Range function - used to generate a range of numbers to loop through

for number in range(a, b):
print(number)

range(a, b, step) will not work on it's own, must be used with another function like above.
last digit won't be included.
the step argument is optional, but without, range iterates by 1.

# While Loops

while something_is_true:

# Global variables

use Global keyword inside a function, to pull variable names from base, to be modified and used.
Don't do often, confusing, and prone to bugs and errors.
Avoid modifying, using is fine, and read it, etc

# Global constant

Values never intended to change.
Example - The value of pi.
The naming convention for this, is all uppercase seperated with underscores.
EX:
PI = 56587106
GOOGLE_URL = http:// etc
Then when calling it later, we see it is all Caps and we know, we don't modify it.
