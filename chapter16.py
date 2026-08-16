"""
Exceptions and Exception Handling in Python

An exception is an error that happens while a program is running.
Python does not crash the whole program immediately if we handle it properly.
Instead, we can catch the error, understand it, and decide what to do.

In simple words:
- Exception = a problem in the program
- Exception handling = a way to deal with that problem safely

Examples of common problems:
- dividing by zero
- using a wrong index in a list
- opening a file that does not exist
- converting a non-numeric value to int

This is very important in real Python, especially in:
- data cleaning
- file handling
- user input validation
- AI/ML projects
"""

# 1) Basic example of an exception
# This will raise ZeroDivisionError
# print(10 / 0)

# 2) try, except, else, finally
# try: code that may fail
# except: code that runs if the error happens
# else: code that runs if no error happens
# finally: code that always runs at the end

a=int(input("Enter your 1st number: "))
b=int(input("Enter your 2st number: "))
try: 
    print(a/b)
except Exception as err:
    print(f"Sorry an error occured as {err}")
else:
    print("no errors occured")
finally:
    print("I always run")

# 3) Common exception types

# ValueError: wrong value for a function
try:
    int("abc")
except ValueError:
    print("ValueError: The value is not valid for conversion.")

# TypeError: wrong type of data
try:
    "hello" + 5
except TypeError:
    print("TypeError: You used a wrong data type.")

# IndexError: index is out of range
numbers = [1, 2, 3]
try:
    print(numbers[10])
except IndexError:
    print("IndexError: Index is out of range.")

# KeyError: key not found in dictionary
student = {"name": "Aisha"}
try:
    print(student["age"])
except KeyError:
    print("KeyError: The key does not exist.")

# FileNotFoundError: file is missing
try:
    file = open("missing_file.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: File does not exist.")

# NameError: variable is not defined
try:
    print(unknown_variable)
except NameError:
    print("NameError: The variable is not defined.")

# 4) Handling multiple exceptions
# You can catch more than one exception in the same block.
try:
    value = int("hello")
except (ValueError, TypeError):
    print("A conversion error happened.")

# 5) Catching all exceptions
# This is useful for general error handling, but not best for beginners.
try:
    result = 10 / 0
except Exception as e:
    print("General exception caught:", e)

# 6) raise keyword
# raise is used to manually create your own exception.
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print("Raised ValueError:", e)

# 7) assert keyword
# assert checks a condition and raises AssertionError if false.
# This is useful for debugging and testing.
num = 10
assert num > 0, "Number must be positive"

# 8) try with user input
# A common real-world example
try:
    user_input = int(input("Enter a number: "))
    print("You entered:", user_input)
except ValueError:
    print("Please enter a valid integer.")

# 9) finally keyword
# finally always runs no matter what.
# It is usually used for cleanup tasks.
try:
    file = open("demo.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("This cleanup code always runs.")

# 10) else keyword
# else runs only if no exception occurs.
try:
    value = 25 / 5
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No error occurred. Result is:", value)
finally:
    print("Program finished.")

# 11) A real-world example: safe calculator
print("\nSimple calculator")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    answer = a / b
    print("Answer:", answer)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter only numbers.")
else:
    print("Calculation was successful.")
finally:
    print("Calculator session ended.")

# 12) Important keywords summary
# try: write risky code here
# except: handle the error here
# else: run this if there is no error
# finally: run this no matter what
# raise: manually trigger an exception
# assert: check a condition and stop if it is false

# 13) Best practice
# Always catch the specific exception instead of catching everything.
# This makes debugging easier and your code more understandable.

# Summary:
# Exceptions are errors that happen during runtime.
# We handle them using try, except, else, finally.
# We can also raise our own exceptions using raise.
# Good exception handling makes programs safe, clean, and user-friendly.
