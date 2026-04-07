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
<<<<<<< HEAD
<<<<<<< HEAD
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

# a comment to a source file
def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
=======
    print(f"[DEBUG] Dividing {a} / {b}")
    if b == 0:
        print(f"[DEBUG] Error: Division by zero!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"[DEBUG] Result: {result}")
>>>>>>> 60cd206 (fix)
    return result
=======
    return a / b
>>>>>>> a1f4914 (Revert "BAD: Add excessive debug logging to calculator module")

def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)
