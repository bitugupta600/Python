'''
n = int(input("Enter the last number: "))
for i in range(1, n + 1):
    print(i,end="")

#print the even number from 1 to 15
for i in range(1,15):
    if i%2==0:
        print(i)


#find the sum of the natural numbers using for loop
n = int(input("Enter the last number: "))
s=0
for i in range(1, n + 1):
    s+=i
print("sum is",s)

#find the sum of even number between 1 to 20

i=1
n=20
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print("Sum",sum)


s = 0
for i in range(1, 21):
    if i % 2 == 0:
        s += i
print("The sum of even numbers  1 and 20 is:", s)

#factorial Number
i=int(input("Enter Number"))
fac=1
while(i>0):
    fac=fac*i
    i=i-1
print("Factorial=",fac)


n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
        factorial=factorial*i
print(f"The factorial of {n} is: {factorial}")

'''

n=int(input("Enter the last number"))
i=n
while(i>=1):
    print(i,end="")
    i+=1
    

















