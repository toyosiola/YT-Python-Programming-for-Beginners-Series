# list comprehension: [item for item in list]
# [expression for item in iterable]
# numbers = [1, 2, 3, 4, 5, 6]

# double_numbers = []
# for number in numbers:
#   new_number = number * 2
#   double_numbers.append(new_number)

# print(double_numbers)

# double_numbers = [number * 2 for number in numbers]
# print(double_numbers)

fruits = ["apple", "banana", "cherry"]
fruits_copy = [fruit.upper() for fruit in fruits]
# print(fruits_copy)

numbers = [number**2 for number in range(1, 6)]
# print(numbers)

# [expression for item in iterable if condition]

even_numbers = [number for number in range(1, 11) if number % 2 == 0]
# print(even_numbers)

letters = [letter.upper() for letter in "python"]
# print(letters)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flattened_list = []
# for row in matrix:
#   # print(row)
#   for num in row:
#     # print(num)
#     flattened_list.append(num)
    
# print(flattened_list)

flattened_list = [num for row in matrix for num in row]
print(flattened_list)