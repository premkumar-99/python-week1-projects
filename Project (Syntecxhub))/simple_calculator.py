"""
Simple Calculator (CLI)
Features:
- Supports +, -, *, / operations and clear
- Validates input and handles divide-by-zero
- Calculation logic separated into functions for testability
- Simple menu to perform repeated calculations or exit
"""
import operator
import sys

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    'x': operator.mul,
    '/': operator.truediv
}

def parse_input(user_input):
    """
    Parse input like '3 + 4' or '3+4' into (num1, op, num2)
    Returns tuple (float, str, float) or raises ValueError
    """
    for op in OPS:
        if op in user_input:
            parts = user_input.split(op)
            if len(parts) != 2:
                raise ValueError("Invalid expression format.")
            a, b = parts
            return float(a.strip()), op, float(b.strip())
    raise ValueError("No valid operator found. Use one of: " + ", ".join(OPS.keys()))

def calculate(a, op, b):
    if op == '/' and b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    func = OPS.get(op)
    if not func:
        raise ValueError("Unsupported operator.")
    return func(a, b)

def menu():
    last_result = None
    while True:
        print("\nSimple Calculator")
        print("Enter expression (e.g. 3 + 4) or:")
        print("  'clear' to reset, 'exit' to quit, 'ans' to use last result")
        user = input(">>> ").strip().lower()
        if user in ('exit', 'quit'):
            print("Goodbye!")
            return
        if user == 'clear':
            last_result = None
            print("Cleared last result.")
            continue
        if not user:
            continue
        # allow using 'ans' in expressions
        try:
            if 'ans' in user and last_result is None:
                print("No last answer stored.")
                continue
            if 'ans' in user:
                user = user.replace('ans', str(last_result))
            a, op, b = parse_input(user)
            res = calculate(a, op, b)
            print(f"Result: {res}")
            last_result = res
        except ZeroDivisionError as e:
            print("Error:", e)
        except ValueError as e:
            print("Input error:", e)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == '__main__':
    menu()
