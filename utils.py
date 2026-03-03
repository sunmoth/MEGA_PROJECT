# utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def calculate(a, b, operation):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operation not in operations:
        raise ValueError("Invalid operation")

    return operations[operation](a, b)
