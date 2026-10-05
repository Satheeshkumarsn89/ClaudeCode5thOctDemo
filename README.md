# Simple Python Calculator

A beginner-friendly console calculator application that performs basic arithmetic operations with error handling.

## Features

- ✅ Basic arithmetic operations: addition, subtraction, multiplication, and division
- ✅ Input validation for numeric values
- ✅ Division by zero protection
- ✅ Unsupported operation detection
- ✅ Continuous operation mode
- ✅ User-friendly interface

## Requirements Met

- Asks user to enter two numbers
- Asks user to choose an operation: +, -, *, /
- Performs calculation and prints result
- Handles invalid input:
  - Non-numeric input detection
  - Division by zero prevention
  - Unsupported operation detection
- Beginner-friendly and readable code
- Uses functions for operations and input validation
- Complete runnable code in one file (calculator.py)

## How to Run

```bash
python3 calculator.py
```

## Sample Input/Output

### Example 1: Simple Addition
```
========================================
Welcome to the Simple Calculator!
========================================
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +

Result: 10.0 + 5.0 = 15.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator. Goodbye!
```

### Example 2: Division
```
Enter first number: 20
Enter second number: 4
Enter operation (+, -, *, /): /

Result: 20.0 / 4.0 = 5.0

Do you want to perform another calculation? (yes/no): yes
Enter first number: 15
Enter second number: 3
Enter operation (+, -, *, /): *

Result: 15.0 * 3.0 = 45.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator. Goodbye!
```

### Example 3: Error Handling - Division by Zero
```
Enter first number: 10
Enter second number: 0
Enter operation (+, -, *, /): /

Error: Cannot divide by zero.

Do you want to perform another calculation? (yes/no): yes
```

### Example 4: Error Handling - Invalid Number
```
Enter first number: abc
Error: Please enter a valid number.
Enter first number: 5
Enter second number: hello
Error: Please enter a valid number.
Enter second number: 3
Enter operation (+, -, *, /): +

Result: 5.0 + 3.0 = 8.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator. Goodbye!
```

### Example 5: Error Handling - Unsupported Operation
```
Enter first number: 7
Enter second number: 2
Enter operation (+, -, *, /): %
Error: Unsupported operation '%'. Please choose from: +, -, *, /
Enter operation (+, -, *, /): -

Result: 7.0 - 2.0 = 5.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator. Goodbye!
```

## Code Structure

- `is_valid_number(value)`: Validates if input is a numeric value
- `get_number(prompt)`: Gets a valid number from user with retry logic
- `get_operation()`: Gets a valid operation with retry logic
- `add(a, b)`: Addition operation
- `subtract(a, b)`: Subtraction operation
- `multiply(a, b)`: Multiplication operation
- `divide(a, b)`: Division operation with zero-check
- `perform_calculation(num1, num2, operation)`: Executes calculation with error handling
- `main()`: Main calculator loop

## Error Handling

The calculator gracefully handles:
- Non-numeric inputs (asks user to re-enter)
- Division by zero (displays error message)
- Unsupported operations (suggests valid options)
- User interruption (Ctrl+C closes gracefully)
