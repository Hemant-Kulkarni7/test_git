str = input("enter string ")
n = len(str)
if str[n-3] == 'i':
    if str[n-2] == 'n':
        if str[n-1] == 'g':
            print(str+'ly')
        else:
            print(str+'ing')
    else:
        print(str+'ing')
else:
    print(str+'ing')