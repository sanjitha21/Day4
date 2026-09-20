"""Explanation of map() and filter() in Python.

map(): applies a function to every item in an iterable and returns a map object.
filter(): keeps only the items for which a function returns True.
"""

# map() example: square each number
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x * x, numbers)
print("map() result:", list(squares))

# filter() example: keep only even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print("filter() result:", list(evens))

# A simple way to remember:
# map() = transform every value
# filter() = select values

# Example with strings
names = ["Alice", "Bob", "Charlie", "Diana"]
long_names = filter(lambda name: len(name) > 4, names)
print("Filtered names:", list(long_names))
