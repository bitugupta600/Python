#Take a list and search specific elements like 2 is present or not if pre
#Enter the number you want to search 
'''
a=[1,2,3,4,5,6,7,8,9,10,2]
n=int(input("Enter the number :"))
if n in a:
    print(n,"Number is present")
else:
    print(n,"Number is Not Present")

#Count the particular elements in a list.
a=[1,2,3,4,5,6,7,8,9,10,5]
n=int(input("Enter the number :"))
c=a.count(n)
print("Particular Element",c)
'''


name = input("Enter your name: ")
lowercase_name = name.lower()
print("Your name in lowercase is:", lowercase_name)
