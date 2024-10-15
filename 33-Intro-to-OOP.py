# Intro to OOP
# Why OOP:
#   - organization
#   - reusability
#   - abstraction
#   - inheritance
#   - polymorphism

# Object: attributes, methods

# class Car:
#   def __init__(self, brand, year):
#     self.brand = brand
#     self.year = year
    
# my_car = Car("Toyota", "2023")
# print(my_car.brand)
# print(my_car.year)
# print(my_car)

# your_car = Car("Chevrolet", "2020")
# print(your_car.brand)
# print(your_car.year)

# class Calculator:
#   def add(self, a, b):
#     return a + b
  
# calc = Calculator()
# summation = calc.add(3, 5)
# print(summation)

class Animal:
  def speak():
    pass
    
class Dog(Animal):
  def speak(self):
    return f"Woof"
  
class Goat(Animal):
  def speak(self):
    return "Baa"
  
class Cat(Animal):
  def speak(self):
    return "Meow"

dog = Dog()
goat = Goat()
cat = Cat()

print(dog.speak())
print(goat.speak())
print(cat.speak())