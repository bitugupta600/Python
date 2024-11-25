'''
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=a+b
print("Add",c)
print("Sub",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Mod",a%b)


a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = a + b

print("Add:", c)
print("Sub:", a - b)
print("Multiplication:", a * b)
print("Division:",a/b)
print("Mod:",a%b)



x = int(input("Enter an initial value for x: "))
print("\nInitial value of x:", x)
x += 5  
print("After x += 5, x =", x)
x -= 3  
print("After x -= 3, x =", x)
x *= 2
print("After x *= 2, x =", x)
x /= 4  
print("After x /= 4, x =", x)
x //= 2 
print("After x //= 2, x =", x)
x %= 3  
print("After x %= 3, x =", x)
x **= 2  
print("After x **= 2, x =", x)




a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
bitwise_and = a & b
print(f"{a} & {b}3 = {bitwise_and} (Bitwise AND)")
bitwise_or = a | b
print(f"{a} | {b} = {bitwise_or} (Bitwise OR)")
bitwise_xor = a ^ b
print(f"{a} ^ {b} = {bitwise_xor} (Bitwise XOR)")
bitwise_not_a = ~a
bitwise_not_b = ~b
print(f"~{a} = {bitwise_not_a} (Bitwise NOT of {a})")
print(f"~{b} = {bitwise_not_b} (Bitwise NOT of {b})")
bitwise_left_shift_a = a << 2
bitwise_left_shift_b = b << 2
print(f"{a} << 2 = {bitwise_left_shift_a} (Left shift of {a} by 2)")
print(f"{b} << 2 = {bitwise_left_shift_b} (Left shift of {b} by 2)")
bitwise_right_shift_a = a >> 2
bitwise_right_shift_b = b >> 2
print(f"{a} >> 2 = {bitwise_right_shift_a} (Right shift of {a} by 2)")
print(f"{b} >> 2 = {bitwise_right_shift_b} (Right shift of {b} by 2)")
'''

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b and a > c:
    print("a is the greatest number")
elif b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")
    



































