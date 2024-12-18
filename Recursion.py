#Recursion
'''
def factorial(x):
    if x==0:
        return 1
    else:
        return (x*factorial(x-1)) #
n=int(input("Enter a number"))
print("factorial is :",factorial(n))
'''
'''
#find sum of natural number using recursion
def sn(n):
    if n==0:
        return 0
    else:
        return n+sn(n-1)
n=int(input("Enter a number"))
r = sn(n)
print("Sum of NM:",r)
'''
'''
def add(x):
    if x == 1:
        return x
    else:
        return x + add(x - 1)

n = int(input("Enter the last number: "))
if n < 0:
    print("Enter a positive integer.")
elif n == 0:
    print("Enter a number greater than 0.")
else:
    print("Sum of natural numbers =", add(n))
'''
'''
#find the Factorial of a number using function without recursion.
def fac(x):
    r = 1
    for i in range(1, x+1):
        r = r * i
    return r

n = int(input("Enter a number"))
print("Factorial of the number ", fac(n))
'''








