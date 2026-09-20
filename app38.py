# List comprehension is a short and readable way to create a list.
# Syntax:
# [expression for item in iterable if condition]

# Example 1: create squares of numbers
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Example 2: keep only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4]

# Example 3: convert names to uppercase
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Same logic written with a normal loop:
squares_loop = []
for n in numbers:
    squares_loop.append(n * n)
print(squares_loop)  # [1, 4, 9, 16, 25]

# List comprehension is useful when the list is created from another list or iterable,
# and the code is simple enough to fit in one line.
