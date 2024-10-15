# Scope
# Scope categories: Local, Global, Enclosing, Built-in
# Scope resolution: LEGB rule
# Ultimately: Where it is defined determines the scope

# Local scope: variable defined inside of a function is localized to that function and can only be accessed in the function


# def print_name():
#   name = "John"
#   print(name)
  
# print(name)

# Global scope: variable defined at the top level of your file or module
# number = 2

# def update_number():
#   number = 5
#   print(number)
  
# update_number()
# print(number)

# Enclosing scope: refers to variables defined in the outer function which can be accessed in the inner function 

# def outer():
#   x = 1
  
#   def inner():
#     print(x)
    
#   inner()
    
# outer()


# name = "John"

# def my_function():
#   name = "James"
  
#   def my_function_2():
#     name = "Jane"
#     print(name)
    
#   my_function_2()
  
# my_function()



# count = 0

# def increment():
#   if count < 2:
#     return 5

  
# count = increment()
# print(count)

number = 6
print(number)
# num1 = 0

# if number > 8:
#   num1 = 5

# print(num1)


