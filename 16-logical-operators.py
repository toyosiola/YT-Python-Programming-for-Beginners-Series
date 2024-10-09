# and: both conditions must be true
# or: at least one condition must be true
# not: negate / invert a certain condition

# condition = True and True

# condition = False or False

# condition = not False
# print(condition)

age = int(input("What is your age? "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen == 'yes':
  print("You are eligible to vote")
  
if age < 18 or age > 120:
  print("You are not within the typical voting age range")
  
if not citizen == 'yes':
  print("You must be a citizen to be eligible to vote")