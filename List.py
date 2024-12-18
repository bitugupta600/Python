#List
#it is collection of different values or diff types of items.
#Ex:
'''    
a=["ram","shyam",12.5]
print(a)
print(a[2])
del a[1]
print(a)
print(type(a))
a[1]="Bitu"
print(a)
'''
'''
l = [3, 5, 7, 8, 9, 2]
s = 0

for i in l:
    s = s + i
print("Sum is:", s)

for i in range(len(l)):
    s=s+l[i]
print("Sum is:",s)
'''

l=[3, 5, 7, 8, 9, 2]
s=0
i=0
while i<len(l):
    s = s+l[i]
    i=i+1
print("Sum is:",s)
