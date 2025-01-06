# *args

def add_numbers(a, b):
  return a + b

def sum_all(*args):
  print(args)
  return sum(args)

def print_all(numbers):
  print(numbers)
  for num in numbers:
    print(num + 2)

# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 20))
print_all(1, 2, 3, 4, 5)

# def greet_all(greeting, *names):
#   for name in names:
#     print(f"{greeting}, {name}")
    
# greet_all("Hello there", "James", "Alice", "Bob", "John")