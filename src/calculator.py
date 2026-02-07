"""Simple calculator operations, including but not limited to add, subtract, multiple, divide, and modulo."""

def add(a, b):
    """Add two numbers."""
    print(f"[DEBUG] Adding {a} + {b}")
    result = a + b
    print(f"[DEBUG] Result: {result}")
    return result

def subtract(a, b):
    """Subtract b from a."""
    print(f"[DEBUG] Subtracting {a} - {b}")
    result = a - b
    print(f"[DEBUG] Result: {result}")
    return result

def multiply(a, b):
    """Multiply two numbers."""
    print(f"[DEBUG] Multiplying {a} * {b}")
    result = a * b
    print(f"[DEBUG] Result: {result}")
    return result

def divide(a, b):
    """Divide a by b."""
    print(f"[DEBUG] Dividing {a} / {b}")
    if b == 0:
        print(f"[DEBUG] Error: Division by zero!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"[DEBUG] Result: {result}")
    return result

<<<<<<< HEAD
def power(a, b):
    """Raise a to the power of b."""
    return a ** b

# a comment to a source file
def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
=======
def factorial(n):
    """Calculate factorial of n."""
    print(f"[DEBUG] Factorial of {n}")
    if n < 0:
        print(f"[DEBUG] Error: Negative number!")
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        print(f"[DEBUG] Base case: returning 1")
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"[DEBUG] Result: {result}")
    return result
>>>>>>> b340993 (Add factorial operation support)
