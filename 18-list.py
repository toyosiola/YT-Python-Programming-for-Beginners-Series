# docs https://docs.python.org/3/tutorial/datastructures.html

import random

days_of_the_week = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
# days_of_the_week[0]= "Sat"
# days_of_the_week.extend(["Thur", "Fri", "Sat"])

# days_of_the_week.insert(2, "Sat")
# print(days_of_the_week[-3])

# random_day = random.choice(days_of_the_week)
# print(random_day)

# IndexError
# print(days_of_the_week[7])
# num_of_items = len(days_of_the_week)
# print(num_of_items)
# print(days_of_the_week[num_of_items - 1])

sibling = ["John", "James"]
parent = ["Doe", "Jane"]
family = [sibling, parent]
# print(family)
print(family[0])
print(family[1])
