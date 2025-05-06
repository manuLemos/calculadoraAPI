import math

def add(a: float, b: float) -> float:

    return a + b

def subtract(a: float, b: float) -> float:

    return a - b

def multiply(a: float, b: float) -> float:

    return a * b

def divide(a: float, b: float) -> float:

    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def sqrt(a: float) -> float:

    return math.sqrt(a)

def exponent(a: float, b: float) -> float:

    return a ** b

def factorial(a: float) -> int:

    return math.factorial(int(a))