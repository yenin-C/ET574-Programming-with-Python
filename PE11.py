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
'''

from math import pi

class Circle():
    Radius = 10
    def __init__(self, radius=1):
        self.radius = radius
