num1 = float(input("Enter your first number: "))
op = input("Enter operator (+, -, *, /)") 
num2 = float(input("Enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("division by zero is not accepted")
    else: print(num1 / num2)
else: print("Invalid operator")

