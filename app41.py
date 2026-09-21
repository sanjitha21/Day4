# map()
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x * x, numbers)
print("map() result:", list(squares))

# filter() 
evens = filter(lambda x: x % 2 == 0, numbers)
print("filter() result:", list(evens))

# Example with strings
names = ["Alice", "Bob", "Charlie", "Diana"]
long_names = filter(lambda name: len(name) > 4, names)
print("Filtered names:", list(long_names))
