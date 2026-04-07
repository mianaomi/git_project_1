"""Simple calculator operations, including but not limited to add, subtract, multiple, divide, and modulo."""
# Temporary comment
"""Basic calculator operations."""
import math

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    print(f"[DEBUG] Dividing {a} / {b}")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"[DEBUG] Result: {result}")
    return result

def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)
    return a / b

def is_positive(n):
    """Check if a number is positive."""
    return n > 0

    #experimenting
