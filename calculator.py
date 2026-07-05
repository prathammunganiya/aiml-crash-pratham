def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add/subtract/multiply/divide): ")

if operation in operations:
    result = operations[operation](num1, num2)
    print("Result:", result)
else:
    print("Invalid operation.")