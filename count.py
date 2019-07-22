'''Write a Python program that accepts a string 
   and calculate the number of digits and letters.'''
   
str = input("Enter string ")
digits = 0
letters = 0
for i in str:
    if(i.isdigit()):
        digits = digits + 1
    elif (i.isalpha() == True):
        letters = letters + 1
print("The number of digits is ",digits)
print("The number of letters is ",letters)