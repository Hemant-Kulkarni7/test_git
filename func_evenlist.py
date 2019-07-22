n = int(input("enter number of elements in the list "))
i = 0 
l = []
print("enter elements")

while i < n:
    x = int(input())
    l.append(x)
    i += 1

def even(s):
    s1 = []
    for i in s:
        if i % 2 == 0:
            s1.append(i)
    print("even numbers list is",s1)

even(l)