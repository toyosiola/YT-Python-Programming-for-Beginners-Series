# states
# instances

class Car:
  def __init__(self, brand, color, year, battery_life=2):
    self.brand = brand
    self.color = color 
    self.year = year
    
my_car = Car("Toyota", "Black", 2022)
your_car = Car("Honda", "Green", 2018)

print(f"I have a {my_car.year} {my_car.color} {my_car.brand} car")
print(f"You have a {your_car.year} {your_car.color} {your_car.brand} car")

# my_car.year = 2024
# print(f"I have upgraded my car to the {my_car.year} model")
