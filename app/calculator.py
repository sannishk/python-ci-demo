"""Interactive calculator with testable functions."""

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def calculate(a, b, op):
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }
    if op not in ops:
        raise ValueError("Unsupported operation")
    return ops[op](a, b)

if __name__ == "__main__":
    # Simple CLI runner so you can try it manually
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ").strip()
        print("Result:", calculate(a, b, op))
    except ZeroDivisionError as zde:
        print("Error:", zde)
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Unexpected error:", e)

