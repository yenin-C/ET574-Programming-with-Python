## Class can be typed directly into programs

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year, color):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.color = color

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} {self.color}"
        return long_name.title()
    
    def car_color(self): #Trying to add a new method for car color
        print(f"This car is {self.color} and I love it!")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


def main():
    #my_used_car = Car()
    my_used_car = Car('subaru', 'outback', 2015, "Sky Blue")
    print(my_used_car.get_descriptive_name())
    print(my_used_car.car_color())

    my_used_car.car_color()

    my_used_car.update_odometer(50_000)
    my_used_car.read_odometer()

    my_used_car.increment_odometer(700)
    my_used_car.read_odometer()
    

main()
