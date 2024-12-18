#WAP to find sum of elements of the list.
'''
a=[]
size=int(input("Enter Elements :"))
for i in range(size):
    val=int(input("Enter Number:"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("Sum of list elements=",sum)

'''
#count total number odd or even in the list.
'''
a=[]
size=int(input("Enter Elements :"))
for i in range(size):
    val=int(input("Enter Number:"))
    a.append(val)
even=0
odd=0
for i in range(size):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("Total Even",even, "Total Odd",odd)
'''
'''
l=[2,3,4,5,6,7,8,9]
#print(max(l))
#print(min(l))
#print((l.reverse))
for i, j in enumerate(l):
    print(i,j)
'''
#reversed()
'''
l = [9, 7, 4, 9, 0, 6]
print(max(l))
print(sum(l))
print(sorted(l))

for i, j in enumerate(l):
    print(i, j)

# List methods
# insert(), pop(), append(), count(), sort(), reverse(), remove(), clear()
'''
'''
l = [9, 7, 4, 9, 0, 6]
l1=sorted(l,reverse=True)
print(l1)
#print(l.sort())
#print(l.index())
#print(l.index(9, 2, 5))
#Program to find the sub list

l1=[1,4,6,7,2,5]
l2=[3,6,7,9,3,4]
for i in range(l1-l2+1):
    if

l1= [3, 5, 4, 6, 5, 2, 6, 6, 8, 7]
l2 = l1[1:7]
print(l2)
print(sum(l2))

'''
'''
l=input("Enter a list between []: ")
lst = eval(l)
start = int(input("Enter the start index: "))
stop = int(input("Enter the stop index: "))
print("Sum =", sum(lst[start:stop+1]))
'''
'''
#take 2 list and print value who is exits in list1
list1=[2,4,6,8]
list2=[8,5,6,8]
cv=[]
#cmp[l1,l2]
#print(cmp)
#result=[value for value in list1 if value in list2]
#print("Value exist in l1",result)
for value in list1:
    if value in list2:
        cv.append(value)
print("value exist in list1",cv)
'''
'''
#take list 1add random value then take a blank list and add even value in list2
l1= [3, 5, 4, 6, 5, 2, 6, 6, 8, 7]
l2=[]
for value in l1:
    if value%2==0:
        l2.append(value)
print("Even value",l2)
'''
#take 1 list and take unique element and put another list2
l1= [3, 5, 4, 6, 5, 4, 6, 6, 8, 7]
ul=[]
for element in l1:
    if element not in ul:
        ul.append(element)
print("UL",ul)











