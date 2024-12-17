
'''
Create a class ETStudent which is used to create instances (objects)
of type ETStudent. 
Use the  __init__() method to assign values for student name and id
Paste the code in the area provided here
'''
class ETStudent:
    def __init__(self, name, id): #self basically means: this instance of the class
        self.id = id #This is the student ID
        self.name = name #This is the student name

'''
1b. Create and use the Student_display() method to print instance variables:  name and id.
with prefix = 'QCC-ET-'
'''
prefix = 'QCC-ET-'

def Student_display(self): #This creates instance variables
    print("Name: ", self.name.title())
    print(f"ID: {prefix} {self.id}")

'''
1c. Instantiate objects of the ETStudent class by calling the class with your own name and id:987654.
'''
yenin_carrion = ETStudent("Yenin Carrion ", 987654) 
#These are the students names and IDs
stevie_bart = ETStudent("Stevie Bart ", 456789)

print(yenin_carrion.name.title(), yenin_carrion.id, sep = '| ') #This will print the student name and id separated by |
print(stevie_bart.name.title(), stevie_bart.id, sep = '| ')


