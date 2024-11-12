## Use the return statement to generate a return value of a functions
## Use input() and while loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break   #use break to exit the infinite while True loop

    l_name = input("Last name: ")
    if l_name == 'q':
        break   #use break to exit the infinite while True loop

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    #print("\nHello ", get_formatted_name(f_name, l_name), '!', sep = '')
