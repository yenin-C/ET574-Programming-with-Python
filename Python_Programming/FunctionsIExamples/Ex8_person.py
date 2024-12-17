# Making an argument optional
## Use the return statement to generate a return value of a function
# In a function definition, the parameters without default values must
# precede the parameters without default values

# creating a function
def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

# calling functions
# arguments passed by position must precede arguments passed by keyword.
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

musician = build_person('Adele', 'Adkins')
print(musician)
