"""
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

print(len(fruits))
print(fruits[1:3])

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)



numbers = [1, 2, 3, 4, 5]

# Append a new number
numbers.append(6)
print("After appending 6:", numbers)

# Remove a specific number
numbers.remove(3)
print("After removing 3:", numbers)

# Slice the list
print("First three numbers:", numbers[:3])
"""

# Create a tuple
fruits = ("apple", "banana", "cherry")

# Try to change an element (This will cause an error)
# fruits[1] = "orange"

# Convert tuple to list
fruits_list = list(fruits)

# Change an element
fruits_list[1] = "orange"

# Convert back to tuple
fruits = tuple(fruits_list)
print("Modified tuple:", fruits)


