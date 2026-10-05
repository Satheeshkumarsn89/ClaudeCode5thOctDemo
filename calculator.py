#!/usr/bin/env python3
"""Simple console calculator application."""


def is_valid_number(value):
    """Validate if the input is a valid number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        user_input = input(prompt).strip()
        if is_valid_number(user_input):
            return float(user_input)
        print("Error: Please enter a valid number.")


def get_operation():
    """Get a valid operation from user."""
    valid_operations = {'+', '-', '*', '/'}
    while True:
        operation = input(
            "Enter operation (+, -, *, /): "
        ).strip()
        if operation in valid_operations:
            return operation
        print(f"Error: Unsupported operation '{operation}'. "
              f"Please choose from: +, -, *, /")


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Error: Cannot divide by zero.")
    return a / b


def perform_calculation(num1, num2, operation):
    """Perform calculation based on the operation."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    try:
        result = operations[operation](num1, num2)
        return result
    except ValueError as e:
        print(e)
        return None


def main():
    """Main calculator loop."""
    print("=" * 40)
    print("Welcome to the Simple Calculator!")
    print("=" * 40)

    while True:
        try:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            operation = get_operation()

            result = perform_calculation(num1, num2, operation)

            if result is not None:
                print(f"\nResult: {num1} {operation} {num2} = {result}\n")

            again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if again not in ('yes', 'y'):
                print("Thank you for using the calculator. Goodbye!")
                break

        except KeyboardInterrupt:
            print("\n\nCalculator closed by user. Goodbye!")
            break


if __name__ == "__main__":
    main()
