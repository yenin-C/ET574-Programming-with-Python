## Demonstrate the scope of global and constant variables

x = 0       # Declare a global variable
PI = 3.14   # Declare a global constant variable
def main():
    print(str(x) + ": function main")
    trivial()
    print(str(x) + ": function main")
    print(f"{PI:.2f} : function main")

def trivial():
    global x
    x += 7
    print(str(x) + ": function trivial")

    global PI
    PI += x

main()
