## Use default string parameter value
## Use the return statement to generate a return value of a function

# creating a function
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"Hello {first_name} {middle_name} {last_name}"
    else:
        full_name = f"Hi {first_name} {last_name}"
    return full_name.title()

# calling functions
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
