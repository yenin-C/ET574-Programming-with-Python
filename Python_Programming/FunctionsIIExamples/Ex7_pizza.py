## Demonstrate a function with arbitrary argument

def main():
    make_pizza(12, "pepperoni")
    make_pizza(16, "mushrooms", 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

main()
