# Some common Exceptions

try:

    import rectangle                #ImportError

    fileName = 'abc.txt'            #FileNotFoundError
    infile = open(fileName, 'r')
    print(infile.readline())

    x = 123
    print(x.upper())                #AttributeError

    letter = "abc"
    print(letter[7])                #IndexError

    d = {'a':"apple", 'b': "banana"}
    word = d['c']                   #KeyError

    print(word123)                  #NameError

    d = {'a':"apple", 'b': "banana"}
    y = d['a']
    print(1 + y)                    #TypeError

    n = 0
    print(1 / n)                    #ZeroDivisionError

except (ImportError, FileNotFoundError) as exc1:
    print(exc1)
except AttributeError:
    print("Exceptions: AttributeError")
except:
    print("Exceptions: Something went wrong.")
    #pass
#else: define a block of code to be executed if no errors were raised
else:
    a, b = "Hello ", "world!"
    print(a+b)
#finally: (optional) will be executed regardless if the try block raises an error or not
finally:
    print("Exception check complete.")
