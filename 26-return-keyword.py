# return keyword (function output)
# no code after the return keyword

# def add_numbers(a, b):
#   return a + b

# def multiply_numbers(c, d):
#   return c * d

# def math_operations(a, b):
#   sum = a + b
#   product = a * b
#   difference = a - b
  
#   return sum, product, difference

# (output) = math_operations(7, 3)
# print(output)

def check_number(num):
  if num > 0:
    return "your number is positive"
  elif num < 0:
    return "your number is negative"
  else:
    return " your number is zero"
  
print(check_number(-9))