# Generators in Python
# A generator is a special type of function that returns an iterator.
# Instead of returning all values at once, it yields one value at a time.
# This makes it memory-efficient for large datasets.

# Example 1: simple generator function

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
print("Example 1: countdown")
for value in countdown(5):
    print(value)

print()

# Example 2: generator vs list

def squares_1_to_5():
    result = []
    for i in range(1, 6):
        result.append(i * i)
    return result

# Generator version

def squares_generator():
    for i in range(1, 6):
        yield i * i

print("Example 2: list version")
print(squares_1_to_5())

print("Example 2: generator version")
for x in squares_generator():
    print(x)

print()

# Example 3: generator expression
# Similar to list comprehension, but lazy and memory-efficient.

gen = (x * 2 for x in range(1, 6))
print("Example 3: generator expression")
print(next(gen))
print(next(gen))
print(next(gen))
print("Remaining values:", list(gen))

print()

# What makes generators useful?
# 1. They save memory.
# 2. They can represent infinite sequences.
# 3. They generate values only when needed.

# Example 4: infinite generator

def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

print("Example 4: first 5 natural numbers")
counter = natural_numbers()
for _ in range(5):
    print(next(counter))

# Summary:
# - Use yield instead of return inside a function to make it a generator.
# - Generators are iterable.
# - They produce values one at a time and pause after each yield.
# - They are ideal for large data streams and lazy evaluation.
