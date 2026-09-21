# Lambda in Python
square = lambda x: x * x
print("Square of 5:", square(5))

add = lambda a, b: a + b
print("Sum of 3 and 7:", add(3, 7))

def my_function(n):
    return lambda x: x * n

double = my_function(2)
print("Double of 10:", double(10))

students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda student: student[1])
print("Sorted students by marks:", students)


