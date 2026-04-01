from dog import Dog
from car import Car, ElectricCar

my_dog = Dog(name="Pluto", age="8")
# print(my_dog)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer = 25
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

my_new_car.increment_odometer(500)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()
