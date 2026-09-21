#exception handling
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


