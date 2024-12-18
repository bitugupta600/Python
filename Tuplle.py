#Tuple
'''
import sys
list1=[1,3,7,9,"ram","shyam"]
tuple1=(1,3,7,9,"ram","shyam")
print("Size of list",sys.getsizeof(list1))
print("Size of tuple",sys.getsizeof(tuple1))
'''
'''
t=(2,'h','anudip',4,5)
print(t)
del t
print(t)
'''
'''
n=(2,'k',5,'the',5,0,3)
#print(n[3])
#print(n[5])
##print(n[-4])
#print(n[1:4])
print(n[:-5])
#print(n[::-1])
'''
'''
# Tuple packing
t = ('Tandra', 37, 'Mumbai')
# Tuple unpacking
#(name, age, address) = t
print(name)
print(age)
print(address)
n=t*2
print(n)
for i in t:
    print(t)


i=0
while i<len(t):
    print([t])
    i+=1

'''

#max
t = ('Tandra', 37, 'Mumbai')
#print(max(t))

#WAP to take sales amount for a particular reason and the
#calculate the total and average sell amount in python in list

sale=[]
n=int(input("Enter sell data : "))
for i in range(n):
    amount=float(input("Enter sales amount"))
    sale.append(amount)
ts=sum(sale)
amount=ts/len(sale)
print("sale amount",sale)
print("total sale",ts)
print("average sale",amount)
m = max(sale) 
n = min(sale)
print("Max Amount :",max(sale))
print("Minimum Value :",min(sale))

    










