##Using as to give a function an alias
from pizza import make_pizza as mp  #an alternate name

def main():
    mp(16, 'pepperoni')
    mp(12, 'mushrooms', 'greenpeppers', 'extra cheese')

main()
