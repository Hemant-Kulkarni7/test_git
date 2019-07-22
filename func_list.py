n = int(input("enter number of elements in the list "))
i = 0 
l = []

while i < n:
    x = int(input())
    l.append(x)
    i += 1

def sum(l):
    s = 0
    i = 0
    for i in l:
        s = s + l[i]
    print("sum of elements of the list is ",s)

sum(l)