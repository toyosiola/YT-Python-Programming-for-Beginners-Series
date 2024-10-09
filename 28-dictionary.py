# What is a dictionary
# Proper formatting of a dictionary
# Accessing data from a dictionary
# Use correct data type for your keys
# Adding new items to your dictionary
# updating values in a dictionary
# Removing a key-value pair
# looping through a dictionary

# unordered
# modifiable
# index by the keys

person = {
  "name": "John",
  "age": 25,
  "city":"New York",
}

# for key in person:
#   print(f"{key}: {person[key]}")

for key, value in person.items():
  print(key)
  print(value)