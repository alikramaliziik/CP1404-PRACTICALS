"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set to True when a valid integer is entered
    except ValueError:  # Catch ValueError specifically
        print("Please enter a valid integer.")
print("Valid result is:", result)
