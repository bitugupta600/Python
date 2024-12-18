#Dictionary
'''
{key:value}

d={}
print(type(d))
d['institute']='Anudip'
d['location']='mumbai'
d['student']=100

print(d)
print(d['location'])
print(d.values())
print(d.keys())


#for Update value
d['location']='delhi'
print(d)

del d['institute']
print(d)
d.clear
print(d)
del d
print(d)

print('locaton' in d)
print('locaton' not in d)
print(len(d))
d1=d.copy()
print(d1)
s=str(d)
print(type(s))
print(d.get('location'))
d2={'marks':98}
d.update(d2)
print(d)
print(d.items())
'''
'''
d={1,4,'b','y','w','j'}
for key in d:
    print(key)
'''
#program to add dictionary

d={1,4,5,7,8,4}
for key in d:
    print(key)


