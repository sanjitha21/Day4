# Generators in Python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Example 1: countdown")
for value in countdown(5):
    print(value)

print()

def squares_1_to_5():
    result = []
    for i in range(1, 6):
        result.append(i * i)
    return result

def squares_generator():
    for i in range(1, 6):
        yield i * i

print("Example 2: list version")
print(squares_1_to_5())

print("Example 2: generator version")
for x in squares_generator():
    print(x)

print()


gen = (x * 2 for x in range(1, 6))
print("Example 3: generator expression")
print(next(gen))
print(next(gen))
print(next(gen))
print("Remaining values:", list(gen))

print()


def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

print("Example 4: first 5 natural numbers")
counter = natural_numbers()
for _ in range(5):
    print(next(counter))

