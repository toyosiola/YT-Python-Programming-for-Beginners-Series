# functions with input
# parameters and arguments

# def welcome(name, location):
#     print(f"Hello {name}!")
#     print("Welcome to the python programming for beginners series")
#     print(f"How is {location} today?")

# positional argument (default)
# keyword argument
# welcome(location = "Los Angeles", name = "Jane")

def multiplication_table(number, stop):
  print(f'Multiplication table {number}')
  
  for i in range(1, stop + 1):
    print(f"{number} x {i} = {number * i}")
    
   
terminate = False

while not terminate: 
  print(f'Multiplication table creator') 
  # take user inputs
  table = int(input("Pick a table (in figure):\n"))
  stop_point = int(input("Where do you you want your table to stop?\n"))

  multiplication_table(table, stop_point)
  user_terminate = input("Do you want to terminate the calculator now? yes/no\n").lower()
  if user_terminate ==  'yes':
    terminate = True