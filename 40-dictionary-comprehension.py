# {key_expression: value_expression for item in iterable}
# {key_expression: value_expression for item in iterable if condition}

# fruits = ["apple", "banana", "cherry"]
# fruits_length = {fruit: len(fruit) for fruit in fruits}
# print(fruits_length)

# fruits_length = {}
# for fruit in fruits:
#   fruits_length[fruit] = len(fruit)
# print(fruits_length)

# squares = {number: number**2 for number in range(1,6)}
# print(squares)

# prices_in_dollars = {"apple": 1.5, "banana": 2.0, "cherry": 2.5}
# prices_in_cents =  {item: price*100 for item, price in prices_in_dollars.items() if price >= 2.0}
# print(prices_in_cents)

grades = {
  "Alice": {"math": 85, "science": 90},
  "Bob": {"math": 75, "science": 80}
}

percentages = {
  student: {subject: grade / 100 for subject, grade in subjects.items()} 
  for student, subjects in grades.items()
}
print(percentages)