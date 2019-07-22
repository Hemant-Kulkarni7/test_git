def swap(a, b):
    c = a
    a = b
    b = c
    print(a,b,c)
    print(id(a))
    print(id(b))
    print(id(c))
    
    return (a, b)
# print(a, b)
x = 10
y = 20
print(swap(x, y))

