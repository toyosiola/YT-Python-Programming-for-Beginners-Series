# nested dictionary
# nested list
# accessing nested dictionary and list

person = {
  "name": "John",
  "age": 30,
  "address": {
    "city": "Springfield",
    "zip": 1234,
    "street": "1234 Main Street"
  },
  "grades": {
    "math": [80, 65, 72, 59],
    "physics": [56, 62, 66, 51]  
  }
}

math_grade = person["grades"]["math"][2]
print(math_grade)

students = [
  {
    "name": "Jane",
    "age": 18,
    "major": "Mathematics"
  },
  {
    "name": "Alice",
    "age": 19,
    "major": "Physics"
  },
  {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
  }
]

alice_major = students[1]["major"]
# print(alice_major)