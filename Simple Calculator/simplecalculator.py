# This is a simple calculator and my first project as a python beginner


num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

operation = input("Enter the op: + , - , / , * ")

if operation == "+":
    print("result: ",  num1 + num2)
elif operation == "-":
    print("result: ",  num1 - num2)
elif operation == "*":
    print("result: ",  num1 * num2) 
elif operation =="/":
    if num2 != 0:
        print("result: ",  num1 / num2)
    else:
        print("Error: Division done by zero")
else:
    print("Invalid Operation")
    