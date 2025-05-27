"""
File handling exercises
"""

# 1. Write user's name to name.txt
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Read name from name.txt and print greeting
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3. Read first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    print(number1 + number2)  

# 4. Read all numbers from numbers.txt and print their sum
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)  
