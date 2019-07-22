#Write a python program to check whether given number is prime

n = int (input("enter a number"))
i=2
if n==1 :
    print(n,"is not a prime number")  
if n==2 :
    print(n,"is a prime number")     
while i < n :
    if n % i == 0:
        print(n,"is not a prime number")
        break
    
    elif i == n-1 :
        print(n,"is a prime number")   
        break
    i +=1
  


   