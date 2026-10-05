# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Simple Python Calculator is a beginner-friendly console application that performs basic arithmetic operations (+, -, *, /) with comprehensive error handling. The entire application is implemented in a single Python file (`calculator.py`).

## Commands

### Running the application
```bash
python3 calculator.py
```

### Linting and code quality
```bash
# Style check with pylint
pylint calculator.py

# Format check with black
black --check calculator.py

# Format code
black calculator.py

# Type hints check with mypy
mypy calculator.py
```

### Testing
The project currently has no formal test suite. If adding tests, use Python's built-in `unittest` module or `pytest`.

## Architecture

**Single-file design**: All code is in `calculator.py` with a clear functional separation:

1. **Input validation layer** (`is_valid_number`, `get_number`, `get_operation`)
   - Handles user input with retry logic for invalid inputs
   - Validates numeric values and supported operations

2. **Operation functions** (`add`, `subtract`, `multiply`, `divide`)
   - Individual functions for each arithmetic operation
   - `divide()` includes zero-check validation

3. **Execution layer** (`perform_calculation`)
   - Uses a dictionary to map operations to functions
   - Handles exceptions from operations (e.g., division by zero)

4. **Main loop** (`main`)
   - Controls the application flow
   - Handles user interactions and repeat logic
   - Catches keyboard interrupt for graceful shutdown

## Code Style

- Functions are small, focused, and well-named
- Input validation is centralized and reusable
- Error messages are user-friendly and specific
- All functions include docstrings
- Entry point uses standard `if __name__ == "__main__"` pattern

## Error Handling

The application handles three categories of errors:
1. **Invalid numbers**: Non-numeric input triggers re-prompt
2. **Unsupported operations**: Invalid operators show valid options and re-prompt
3. **Division by zero**: Caught and displays error message, allows retry

Keyboard interrupt (Ctrl+C) is caught for clean shutdown.
