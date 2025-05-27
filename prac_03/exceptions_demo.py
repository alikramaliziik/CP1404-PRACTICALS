"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When I input a non-integer (e.g., a decimal or string) as numerator or denominator.
2. When will a ZeroDivisionError occur? When I input zero as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, by checking if the denominator is zero before division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
