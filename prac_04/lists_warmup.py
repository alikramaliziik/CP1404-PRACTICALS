# Lists Warmup
numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] -> This is the first element in the list: 3
# numbers[-1] -> This is the last element in the list: 2
# numbers[3] -> This is the fourth element in the list: 1)
# numbers[:-1] -> This returns a slice of the list from the last element up to but not including the first element: [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> This returns a slice of the list from index 3 up to but not including index 4: [1]
# 5 in numbers -> This returns True as 5 is present in the list
# 7 in numbers -> This returns False as 7 is not present in the list
# "3" in numbers -> This returns False as "3" is a string and the list contains only integers
# numbers + [6, 5, 3] -> This concatenates the list [6, 5, 3] to numbers, resulting in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element to "ten"
numbers[0] = "ten"
# Change the last element to 1
numbers[-1] = 1
# Print all elements from numbers except the first two (slice)
print(numbers[2:])
# Print whether 9 is an element of numbers
print(9 in numbers)
