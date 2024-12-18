#multiplication table display
'''
n=int(input("Enter Number you want to display"))
for m in range(1,11):
    print(n*m)
    
#while loop
n=int(input("Enter Number you want to display"))
m=1
while(m<=10):
    print(n*m)
    m=m+1


for i in range(2,21,2):
    print(i)


#sum of digit
n=int(input("Enter Number "))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print("Sum",sum)
#####

n=int(input("Enter a number"))
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print("Sum of the digits is:",s)
'''
'''
n=int(input("Enter Number you want to count"))
c=0
while n!=0:
      n=n//10
      c=c+1
print("Number of digits:",c)
'''
'''
n=345
345!=0-false
n=345//10 R-5
C=0+1//c=1
2nd step:
n=34
34!=0-false
n=34/10 R-4
c=1+1=2, c=2
3rd step:
n=3
n=3!=0, false
n=3/10
'''
'''
i=int(input("Enter a Number"))
fac=1
while(i>0):
    fac=fac*i
    i=i-1
print("Factorial of the number ",fac)
'''


'''
y=int(input("Enter Year"))
if(y%4==0 and y%100!=0) or (y%400==0):
      print("leap year")
else:
    print("Not leap year")


#write a program to give factors of the number
n=int(input("Enter A number"))
for i in range(1,n,1):
    if (n%i)==0:
        print(i)


n=int(input("Enter a Number"))
if(n>=1):
    print("Positive Number")
elif(n<0):
    print("Negative Number")
else:
    print("Zero")

'''

def msg(x=10):
    print(x)
msg(5)



















