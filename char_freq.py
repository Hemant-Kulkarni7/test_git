'''Write a Python program to count the number
   of characters (character frequency) in a string.'''
   
str = input("enter string ")  
d = {}
for n in str:
        key = d.keys()
        if n in key:
            d[n] += 1
        else:
            d[n] = 1
print(d)            