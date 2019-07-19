n = int (input("enter a number"))
i=2
while i < n :
    if n % i == 0:
        print(n,"is not a prime number")
        break
    
    elif i == n-1 :
        print(n,"is a prime number")   
        break
    i +=1
if n==1 :
    print(n,"is not a prime number")    


   