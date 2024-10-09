# docstring is a special type of comment used to describe the purpose function

def add_numbers(a, b):
  """It accepts two numbers and returns the result

  result: number or float => a + b
  """
  return a + b

print(add_numbers.__doc__)