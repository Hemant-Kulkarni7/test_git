str = input("enter string ")

def rev (s):
    str1 = ''
    for i in s:
        str1 = i + str1
    print("the reversed string is",str1)

rev(str)