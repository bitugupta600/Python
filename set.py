#set in python
# { ...........}
'''
s={1,2,3,(4,5,7)}
print(s)
print(type(s))

s1=set([1,2,3,4,5])
print(s1)
print(type(s1))


s={3,6,7,7,5,3,"Hello", "Hii","Hii"}
print(s)
print(len(s))
print(s)

for i in s:
    print(i,end=" ")

#ADD() method
#Update() method
s.add(10)
print(s)
s.update([1,3,4])
print(s)
s.discard("Hii")
print(s)
s.discard(15)
print(s)
s.remove("Hello")
print(s)
s.remove(7)
print(s)
'''
'''
#take a dataset remove the dublicate value
s={4,5,6,4,4,3,4,3,5,5,8,9,5,6,7,7,5,5,'a','a','b'}
print(s)

data=[4,5,6,4,4,3,4,3,5,5,8,9,5,6,7,7,5,5,'a','a','b']
unique_data=list(set(data))
print("Unique data is ",unique_data)
'''
'''
a={1,2,3,4,5}
b={4,5,6,7,8}

print(a|b)

print(a.union(b))
print(a&b)
print(a.intersection(b))
print(a-b)
print(a.difference(b))

print(a^b)
#print(a.symmetric_difference(b))
print(a.intersection(b))
print(a&b)
print(a)

print(a.symmetric_difference(b))
a.symmetric_update(b)
print(a)

#a.clear()
print(a)
b=a.copy()
print(b)

a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)

a={1,2,3,4,5}
a.frozenset([2,6,8,9,11])
print(a)
#for i in a:
   # print(i)
'''
d={2:"Anudip","A":20}
f=frozenset(d)
print(f)



