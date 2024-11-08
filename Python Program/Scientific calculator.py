import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def exp(x):
    return math.exp(x)

def log(x):
    if x <= 0:
        return "Error: Logarithm of non-positive number"
    else:
        return math.log(x)

def main():
    print("Welcome to My Scientific Calculator!")
    print("Supported operations: +, -, *, /, sin, cos, tan, exp, log")
    print("Enter 'quit' to exit")

    while True:
        expression = input("Enter an expression: ")

        if expression.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()