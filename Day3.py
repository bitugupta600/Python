'''#value_if_true if condition else value
#Ternary_operator
n=int(input("Enter A Number"))
s="Even" if n%2==0 else "odd"
print(s)
'''
'''
#swapping 1st Method
#SI:p*r*t/100
#simple interest
p=int(input("Enter Pricipal Amount"))
r=int(input("Enter Rate of interest"))
t=int(input("Enter Time"))
SI=p*r*t/100
print("Simple Interest is:",SI)
'''

'''
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=a
a=b
b=c
print("After swap A value is :",a)
print("After swap B value is :",b)
'''
'''
a=int(input("Enter a value"))
b=int(input("Enter b value"))
a=a+b
b=a-b
a=a-b
print("After swap A value is :",a)
print("After swap B value is :",b)

'''

'''
a,b=10,20
print("bedfore Interchange :a=",a," and b=",b)
a, b=b,a
print("After interchange: a=",a," and b=",b)
'''


'''
#A program to convert killometers to miles
# 1 kilometer = 0.621371 miles
k=int(input("Enter Killometrs you want to convert miles:"))
m=0.621371
n=k*m
print("Miles ",n)
'''
'''
#Control Flow Statement
if(Condition):
print("hello")
print("Hii")
print("Welcome")

#conditional Statement
if
if else
if elif else
nested if else
'''
'''
n=int(input("Enter a number:"))
if(n==0):
    print("You have entered Zero")
elif n==1:
     print("You have Entered One")
elif n==2:
    print("You Have Entered Two")
else:
    print("Entered Wrong Number")
print("End of the program")
'''
'''
n=int(input("Enter A Number"))
if(n>0):
    print("Number is positive")
elif(n<0):
    print("Number is negative")
else:
    print("Zero")
'''
'''
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=int(input("Enter 3rd Number"))
if(a>b):
    if(a>c):
        print(a," is largest")
    else:
        print(c,"is largest")
else:
    if(b>c):
        print(b,"(is largest")
    else:
        print(c,"is largest")
 '''



'''
#even-odd+vote or not
n=int(input("Enter a Number"))
if(n%2==0):
    print("Number is Even")
else:
    print("number i odd")
    

n=int(input("Enter Age"))
if(n>=18):
    print("Eligible for voting")
else:
    print("Not Eligible for Voting")
'''
#Find a Grade of Student 
#s1,s2,s3,Total, Average,if(av>=90-A-grade,av>=70-B-Grade,av>50-c-grade,av>=40-Pass,av<40-"fail"

s1=int(input("Enter subject1 marks"))
s2=int(input("Enter subject2 marks"))
s3=int(input("Enter subject3 marks"))
t=s1+s2+s3
av=t/3
print("Total Marks is :",t)
print("Average Marks is:",av)
if(av>=90):
      print("A-Grade")
elif(av>=70):
    print("B-Grade")
elif(av>=50):
    print("C-Grade")
elif(av>=40):
     print("Pass")
else:
    print("fail")

















      

