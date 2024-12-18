'''
def msg():#definition
    print("hello world")
msg()#calling
msg()
'''
'''
def msg():
    a=int(input("Enter 1st Number"))
    b=int(input("Enter 2nd Number"))
    c=a+b
    print("Addition",c)
msg()
msg()
'''
'''
def fun(n):
    for i in range(10):
        print("*",end="")
    print()
n=int(input("Enter the number of rows"))
for i in range(n):
    fun(5)
   
'''


'''
#NANR
def msg():
    a=int(input("Enter 1st Number"))
    b=int(input("Enter 2nd Number"))
    c=a+b
    print("Addition",c)
msg()
'''

'''
#NAWR
def add():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    c=a+b
    return c
x=add()
print("Addition",x)
'''
'''
#With argument no return
def add(a,b):
    c=a+b
    print("Addition",c)
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
add(a,b)
'''
'''
#WAWR
def add(a,b):
    c=a+b
    return c
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
x=add(a,b)
print("Add",x)
'''

#find the area of rectangle through function.

def msg(l, w):
    area = l * w
    return area

l = 10
w = 20
area = msg(l, w)
print("Area of rectangle:", area)









