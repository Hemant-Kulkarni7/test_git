n = int(input("enter number "))
x = int(input("enter minimum range "))
y = int(input("enter maximum range "))

def ran(a,b,c):
    if a in range(b,c):
        print(a,"is in the given range")
    else:
        print(a,"is not in the given range")

ran(n,x,y)