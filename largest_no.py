#Write a Python program to get the largest number from a list.

n = int(input("Enter number of elements "))
l1 = []
i = 0
print("enter elements of list")
while i < n:
    x = int(input())
    l1.append(x)
    i += 1
num = l1[0]
for no in l1:
    if no > num:
        num = no
print("Largest no is ", num)