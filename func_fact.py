n = int(input("enter a number "))

def fact(x):
    m = x
    num = 1
    while x > 0:
        num = num * x
        x -= 1
    print("factorial of",m,"is",num)    
    
if n < 0:
    print("enter positive integer number")
else:
    fact(n)    