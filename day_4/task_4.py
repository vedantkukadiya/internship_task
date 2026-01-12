# menu based calculator
def add(x, y):
    return x + y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x/y

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

ch=input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if ch=='1':
    print(add(num1,num2))
elif ch=='2':
    print(subtract(num1,num2))
elif ch=='3':
    print(multiply(num1,num2))
elif ch=='4':
    print(divide(num1,num2))
else:
    print("Invalid input")