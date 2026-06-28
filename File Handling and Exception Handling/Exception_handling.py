# An exception is an error that occurs while the program is running, like:

# dividing by zero → ZeroDivisionError

# opening a missing file → FileNotFoundError

# using wrong type → TypeError

# Exception handling = catching those errors so your program doesn’t crash, and responding gracefully

# Basic try–except

# Pattern:
# try:
#     risky_code_here
# except SomeErrorType:
#     handle_error_here

# Example: division:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# File handling with exceptions

filename = "data.txt"

try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the name/path.")

# Multiple exceptions

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Number cannot be zero.")

# else and finally

# Structure:

# try:
#     # code that might raise an exception
# except SomeError:
#     # runs if that error occurs
# else:
#     # runs if NO exception happens
# finally:
#     # runs ALWAYS (cleanup)

# Example with file:

try:
    f = open("example.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File missing")
else:
    print("File read successfully")
finally:
    try:
        f.close()
    except NameError:
        pass  # f never opened