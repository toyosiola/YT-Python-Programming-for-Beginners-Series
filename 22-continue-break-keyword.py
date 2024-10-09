# - break exits the loop entirely
# - continue skips the current iteration and moves on to the next one.


# days_of_the_week = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]

# for day in days_of_the_week:
#   if day == "Tues":
#     continue
#   print(day)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list_of_numbers:
  if i % 2 != 0:
    continue
  print(i)

