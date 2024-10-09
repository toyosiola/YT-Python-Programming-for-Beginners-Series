# user_input = int(input("Pick a number: "))

# if user_input > 0:
#   print("Your number is positive")
#   # check if number is even or odd
#   if user_input % 2 == 0:
#     print("Ypu number is also an even number")
#   else:
#     print("Your number is also an odd number")  
# else:
#   print("Your number is negative")

# if user_input > 0:
#   print("Your number is positive")
# elif user_input < 0:
#   print("Your number is negative")
# else:
#   print("Your number is zero")

age =  int(input("What is your age? "))

if age < 0:
  print("Invalid age")
elif age <= 12:
  print("You are a child")
elif age <= 17:
  print("You are a teenager")
elif age <= 29:
  print("You are a young adult")
elif age <= 64:
  print("You are an adult")
else:
  print("You are a senior")
