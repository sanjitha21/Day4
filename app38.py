# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4]

names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

squares_loop = []
for n in numbers:
    squares_loop.append(n * n)
print(squares_loop)  # [1, 4, 9, 16, 25]


