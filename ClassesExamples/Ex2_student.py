## creating user-defined classes

# Create a class ETStudent which is used to create instances(objects)
# of type ETStudent.
class ETStudent:
    # A function that is part of a class is called a 'method'.
    # The __init__ method runs whenever we create a new instance
    # of the class ETStudent. It is used to initialize
    # ETStudent instance variables.
    # Use the __init__() method to assign values for name and id
    def __init__(self, name, id):
    # self must come first before the other parameters.
        self.name = name    # name is an attribute of ETStudent class
        self.id = id        # id is an attribute of ETStudent class

    # Use the display() method to print instance variables, name and id.
    def display(self):
        prefix = 'QCC-ET-'
        print("Name:",self.name.title())
        print(f"Id: {prefix}{self.id}")

# Instantiate objects of the ETStudent class
# A class variable is visible to all instances of a class,
# and does not vary from instance to instance.
s1 = ETStudent("john smith", 123456)
s1.display()

s2 = ETStudent('tom cat', 101)
s2.display()

s3 = ETStudent('jerry mouse', 202)
s3.display()

#Access and print the attribute values
print(s1.name.title(), s1.id, sep = '|')
print(s2.name[:3].title(), s3.name[0:5].title(), sep = " & ")
