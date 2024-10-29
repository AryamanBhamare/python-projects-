num1 = float(input("enter no. 1"))
num2 = float(input("enter no.2"))
op = input("enter operators (+,/,*,%,-)")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
elif op == "%":
    result = num1 % num2
else:
    print("wrng input")

print("Result = " , result)
