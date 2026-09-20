# Exception handling in Python
# It helps us manage runtime errors without stopping the program.
# try: code that may raise an exception
# except: handles the exception
# else: runs only if no exception occurs
# finally: runs no matter what

print("Exception handling example:\n")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
else:
    print(f"Division result = {result}")
finally:
    print("This block always executes.")

# Another example with a custom error scenario
print("\nAnother example:\n")

try:
    marks = [90, 80, 70]
    print(marks[5])
except IndexError:
    print("Error: Index is out of range.")
