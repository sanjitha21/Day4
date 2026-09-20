# Lambda in Python
# A lambda is an anonymous function used for short, one-line operations.
# It can take any number of arguments, but it has only one expression.

# Example 1: Simple lambda with one argument
square = lambda x: x * x
print("Square of 5:", square(5))

# Example 2: Lambda with two arguments
add = lambda a, b: a + b
print("Sum of 3 and 7:", add(3, 7))

# Example 3: Using lambda inside another function

def my_function(n):
    return lambda x: x * n

double = my_function(2)
print("Double of 10:", double(10))

# Example 4: Sorting with lambda
students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda student: student[1])
print("Sorted students by marks:", students)

# Explanation:
# lambda arguments: expression
# It is useful when we need a quick function without defining a full def block.
