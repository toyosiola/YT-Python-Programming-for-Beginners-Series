class Car:
  def __init__(self, brand, color, year, battery_life=2):
    self.brand = brand
    self.color = color 
    self.year = year
    self.battery_life = battery_life
    
  def display_info(self):
    print(f"Car brand: {self.brand}, Color: {self.color}, Year: {self.year}, Battery life: {self.battery_life}")

my_car = Car("Toyota", "White", 2023, 5)
print(my_car.brand)
my_car.brand = "Honda"
print(my_car.brand)
# print(my_car.color)
# print(my_car.year)
# print(my_car.battery_life)
# print(my_car.display_info())

class Dog:
  def __init__(self, name):
    self.name = name
    
  def speak(self):
    print(f"{self.name} says Woof!")

# my_dog = Dog("Buddy")
# my_dog.speak()