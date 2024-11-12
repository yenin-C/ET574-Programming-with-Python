## Passing Arguments

# creating a function
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#Positional Arguments – order matters
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')

#Keyword Arguments – order does not matter
describe_pet(pet_name = 'harry', animal_type = 'hamster')
