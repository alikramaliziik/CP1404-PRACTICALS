import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Answers to random function questions:
# Line 1: random.randint(5, 20)
#   - Smallest number: 9
#   - Largest number: 12

# Line 2: random.randrange(3, 10, 2)
#   
#   - Smallest number: 7
#   - Largest number: 9
#   - Could it produce a 4? No, because randrange(3, 10, 2) generates numbers in [3, 5, 7, 9]

# Line 3: random.uniform(2.5, 5.5)
#   
#   - Smallest number: 3.4489336005141418
#   - Largest number: 3.8574212891919535


# Code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
