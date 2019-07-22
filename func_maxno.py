print("enter 3 numbers")
i = 0
l = []

while i < 3:
    x = int(input())
    l.append(x)
    i += 1

def max_no(a,b,c):
    if a > b:
        if a > c:
            print (a,"is the maximum of 3 numbers")
        else:
            print (c,"is the maximum of 3 numbers")  
    elif b > c:
        print (b,"is the maximum of 3 numbers")
    else:
        print (c,"is the maximum of 3 numbers")             

max_no(l[0],l[1],l[2])  