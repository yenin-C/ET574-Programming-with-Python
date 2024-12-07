'''
3. Import Class
a) Import pi only from math module.
b) Implement a class Circle with an attribute, radius.
c) Implement an init method with an optional parameter type.
Set the default value of the attributes of radius to 1.
d) Implement a display method to print the value of radius.
e) Implement a setRadius method to assign radius to the instance variable.
f) Implement a getRadius method to return the value of the instance variable radius.
g) Implement an area method to return the value of area of a circle.
h) Implement a circumference method to return the value of circumference of a circle.
i) Save Rectangle class and Circle class as shapes.py.
j) Import Rectangle class and Circle class from shapes.py.
k) Employs the Rectangle class methods and Circle class methods above and set and get various measurements of a
rectangle and a circle.
'''
# shapes.py
from math import pi         # Import pi only from math module

class Circle:           # Implement a class Circle with an attribute, radius.
    def __init__(self, radius = 1):         # Implement an init method with an optional parameter type
        self.radius = radius

    def display(self):          # Implement a display method to print the value of radius.
        print(f"Radius: {self.radius}")

    def setRadius(self, radius):            # Implement a setRadius method to assign radius to the instance variable
        self.radius = radius

    def getRadius(self):            #Implement a getRadius method to return the value of the instance variable radius
        return self.radius
   
    def area(self):         # Implement an area method to return the value of area of a circle
        return pi * self.radius ** 2
   
    def circumference(self):            # Implement a circumference method to return the value of circumference of a circle
        return 2 * pi * self.radius
   

class Rectangle:
    def __init__(self, length = 1, width = 1):
        self.length = length
        self.width = width
        
    def display(self):
        print(f'Length: {self.length}, Width: {self.width}')
        
    def setLength(self, length):
        self.length = length
        
    def setWidth(self, Width):
        self.width = Width
        
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
