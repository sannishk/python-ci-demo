## Calculator program - test pipleine run
def run_calculator():
    """Interactive calculator that asks for two numbers and an operation.
    Returns the numeric result (float) or None if operation is invalid.
    """
    print("Welcome to Calculator!")
    # Ask the user for two numbers.
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Ask the user to choose an operation.
    print("Choose operation: +, -, *")
    op = input("Enter operation: ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    else:
        print("Invalid operation")
        return None

    print("Result:", result)
    return result

if __name__ == "__main__":
    run_calculator()
