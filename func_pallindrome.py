str = input("enter string ")

def pallindrome (s):
    str1 = ''
    for i in s:
        str1 = i + str1
    if (s == str1):
        print("string is pallindrome")
    else:
        print("string is not pallindrome")

pallindrome(str)        
