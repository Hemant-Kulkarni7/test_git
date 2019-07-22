n = int(input("enter number of elements in the list "))
i = 0 
l = []
print("enter elements")

while i < n:
    x = int(input())
    l.append(x)
    i += 1

def uniq(s):
    s1 = []
    for i in s:
        if i in s1:
            continue
        else:
            s1.append(i)
    print("unique list is",s1)

uniq(l)