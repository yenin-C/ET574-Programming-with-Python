## Demonstrate the scope of variables

def main():
    ## Demonstrate the scope of local variable
    x = 5
    trivial()

def trivial():
    print(x)

main()
