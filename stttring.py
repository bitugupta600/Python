'''
s="i love 34 india"
print(s.isalnum())
#print(s)

#a="RAM"
##print(a.isdigit())
#print(a.isalpha())
#print(a.isupper())
#print(a.islower())
#print(a.isupper())
#print(a.len())
s=".....Anudip...."
#l=["1","2","3"]
#str=s.join(l)
#print(str)
#print(
#print(s)
##print(s.rstrip("."))
#print(

#s="python is a programming language"
#print(s.split("a"))
#WAP to count the number of times character appears in a stream
def count(s,c):
    return s.c(char)
s="python is a programming language"
char='s'
result=count(s,c)
print("Character",c, appears result)



#for i in range(1,11):
 #   print("Table Five :",5*i)

s=int(input("Enter the starting number:"))
e=int(input("Enter the ending number :"))
print("Even number series:")
for i in range(s,e+1):
    if i%2==0:
        print(i)


l=["Cofee","Tea","Sugar","Bread","spong","Cherry"]
for item in l:
    print(item)


s=0
for i in range(1,11):
    s+=i
print("sum of number 1 to 10:",s)

i = 0
while i < 5:  
    j = 0
    while j <= i:  
        print('*', end=' ')
        j = j + 1
    print()  
    i = i + 1


r=5
for i in range(1,r+1):
    s=r-i
    st=2*i-1
    print(" "* s+ "*" * st)



print("The first 10 natural number are:")
for i in range(1,11):
    print(i)
    

def palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
string=input("Enter a String:")
if palindrome(string):
    print(string ,"is a Palindrome.")
else:
    print(string, "is not a palindrome.")
    
'''
i=int(input("Enter Number:"))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print("Palindrome Number")
else:
    print("Not Palindrome Number")


















