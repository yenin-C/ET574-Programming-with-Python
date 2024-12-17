## Store classes in modules
## Use Import to bring the specific class to the program
from car import Car, Battery
from random import choice

my_used_car = Car('audi', 'a4', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.odometer_reading = 23
my_used_car.read_odometer()
my_used_car.increment_odometer(200)
my_used_car.read_odometer()
my_used_car.update_odometer(500)
my_used_car.read_odometer()
print()


lst = [75, 100]
batSize = choice(lst)
my_new_car = Car('tesla','s', 2021)
print(my_new_car.get_descriptive_name())
my_new_car = Battery(batSize)
my_new_car.describe_battery()
my_new_car.get_range()
