'''Write a Python program to add 'ing' at the end of a given 
   string (length should be at least 3). If the given string already
   ends with 'ing' then add 'ly' instead. If the string length of the given
   string is less than 3, leave it unchanged.'''

str = input("enter string ")
n = len(str)
while n > 3:
    if str[n-3] == 'i':
        if str[n-2] == 'n':
            if str[n-1] == 'g':
                print(str+'ly')
                break
            else:
                print(str+'ing')
                break
        else:
            print(str+'ing')
            break
    else:
        print(str+'ing')
        break