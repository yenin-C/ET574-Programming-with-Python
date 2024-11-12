## Use default parameter value

# creating a function
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# calling function
describe_pet('willie')

def my_pet(pet_name, pet_type = "cat", pet_gender = 'female'):
    print(f"I have a {pet_type}.")
    print(f"my {pet_type}'s name is {pet_name.title()}.")
    print(f"My {pet_type} is a {pet_gender}.")


my_pet("mishu")
