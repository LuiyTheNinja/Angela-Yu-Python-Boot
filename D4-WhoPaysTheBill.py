import random
# Challenge: Using provided friends list. 
# Print out a random one of the names
# Each time, code runs, a different name should be printed. 

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


# 2 different ways. 
print(random.choice(friends))

random_index = random.randint(0, 4)
print(friends[random_index])