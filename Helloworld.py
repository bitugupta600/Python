'''x = 10  # Global variable

def my_function():
    y = 20  # Local variable
    global x
    x += 5
    print("Inside function, x:", x, "y:", y)

my_function()
print("Outside function, x:", x)

def example_function():
    print("This line is correctly indented.")
      print("This line has incorrect indentation.")  # IndentationError

example_function()



name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("\n--- Details ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f} meters")
'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("\n---Details---")
print("Name",name)
print("Age",age)
print("Height",height)
