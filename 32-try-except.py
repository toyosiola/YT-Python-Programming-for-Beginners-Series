# try:
#   number = int(input("Enter a number: "))
#   div = 20 / number
#   print(div)
# except ValueError:
#   print("Please, enter a valid integer")
# except ZeroDivisionError:
#   print("Division be zero is not allowed")

# try:
#   number = int(input("Enter a number: "))
#   div = 20 / number
# except (ValueError, ZeroDivisionError) as error:
#   print(f"Error: {error}")
# else:
#   print(div)
# finally:
#   print("Mathematical operation completed")

try:
  age = int(input("Please enter your age: "))
  if age < 0:
    raise ValueError("Age cannot be negative")

except ValueError as error:
  print(f"Error: {error}")

# - Error handling
# - Common errors
# - Try-except 
# - Handling multiple exceptions, handling generic exceptions
# - else clause
# - finally clause
#  - raising exceptions
