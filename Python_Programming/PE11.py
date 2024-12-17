'''
1. Class Implementation
a) Implement a class Rectangle with two attributes, width and height.
b) Implement an init method with an optional parameter type.
Set the default value of the attributes of width and height to 1.
c) Implement a display method to print the values of width and height.
d) Instantiate two objects of type rectangle, one with arguments one without.
r1 = Rectangle(4, 5)
r2 = Rectangle()
e) Call display() to print width and height.
f) Access and print the attribute values of r1 and r2.
'''
class Rectangle:
    def __init__(self, name=1, width=1, height=1):
        self.name = name
        self.width = width
        self.height = height

    def display(self):
        print(self.name, self.width, self.height)

r1 = Rectangle("r1")
r1.display()

r2 = Rectangle("r2", 4, 5)
r2.display()

print(r1.name, r1.width, r1.height)
print(r2.name, r2.width, r2.height)

print('\n')

# 3
# main.py
from shapes import Circle, Rectangle

circle = Circle()
circle.setRadius(10)
circle.display()
print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")

print()

rectangle = Rectangle()
rectangle.display()
rectangle.setLength(4)
rectangle.setWidth(3)
print(rectangle.getLength())
print(rectangle.getWidth())
print(rectangle.area())
print(rectangle.perimeter())
