n = int(input("enter number of elements in the list "))
i = 0 
l = []
print("enter elements")

while i < n:
    x = int(input())
    l.append(x)
    i += 1

def mul (l):
    m = 1
    i = 1
    for i in l:
        m = m * i
    print ("multiplication of all elements in the list is",m)

mul(l)        