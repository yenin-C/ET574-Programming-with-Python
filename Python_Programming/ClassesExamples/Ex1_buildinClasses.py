## Demonstrate the built-in classes using various functions and methods

s = "Hello World!"
print(type(s))
print(id(s))
print(len(s))
print(s.upper())
print(s.lower())
print()

L = [1, 2, 3]
print(type(L))
print(id(L))
print(len(s))
L.insert(0, 'apple')
L.append(247)
print(L)
print()

t = ('apple', 'banana', 'cherry', 'apple')
print(type(t))
print(id(t))
print(len(t))
x = t.index('apple')
y = t.count('apple')
z = t[0][0]
print(x, y, z)
print()

d = {'name': 'john', 'age': 20}
print(type(d))
print(id(d))
print(len(d))
print(d.get("name"))
d.update({"age": 22})
print(d.values())
