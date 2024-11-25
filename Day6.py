#wap take a list of sales amount and classify itself if sales>500 then print
#High amount sales if < then low amount
'''
n=int(input("Enter sales amount"))
if(n>=500):
    print("High seles amount")
else:
    print("Low seles amount")
'''
#Enter some sales amount from keyboard using loop find total and average
'''
print("Enter 5 sales amount")
ts=0
for i in range(5):
    sa=int(input("Enter sales amount"))
    ts=ts+sa
    av=ts/5
print("sales amount",ts)
print("Average ",av)

#WAP to find the reverse of a number.
n=int(input("Enter a number"))
r=0
while(n!=0):
    r=n%10
    r=r*10+r
    n=n//10
print("Reverse of number",r)
'''
'''
n=int(input("Enter number"))
rev=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("Reverse",rev)
'''
'''
n=int(input("Enter A number"))
rev=0
i=1
x=1
while(i>0):
    rev=rev*10+i%10
    i=i//10
if(x==rev):
    print("palindrome Number")
else:
    print("Not Palindrome Number")

'''

n=int(input("Enter A number"))
rev=0
x=n
while n>0:
    rev=rev*10+n%10
    n=n//10
if(x==rev):
    print("palindrome number")
else:
    print("Not Palindrome ")







