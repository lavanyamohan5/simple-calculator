# simple-calculator
a simple calculator using python
# Tkinter Calculator

A simple calculator application built using Python's Tkinter library. This calculator supports basic arithmetic operations, trigonometric functions, square root, and percentage calculations.

## Features

- Basic arithmetic operations: Addition, Subtraction, Multiplication, Division
- Trigonometric functions: Sine, Cosine, Tangent (input in degrees)
- Square root calculation
- Percentage calculation
- Clear and Equals functionality

## Prerequisites

- Python 3.x
- Tkinter (comes pre-installed with standard Python distribution)

## Installation

1. Ensure Python 3.x is installed on your machine.
2. Clone the repository or download the script file.

## Usage

1. Run the script using Python:
    ```bash
    python calculator.py
    ```

2. A window titled "CALCULATOR" will open.

3. Use the buttons on the calculator interface to perform calculations:
    - **Numbers (0-9)**: To input numbers.
    - **Operators (+, -, *, /)**: To perform arithmetic operations.
    - **Trigonometric Functions (sin, cos, tan)**: To calculate sine, cosine, and tangent values (input in degrees).
    - **Square Root (^)**: To calculate the square root of a number.
    - **Percentage (%)**: To calculate the percentage of a number.
    - **Clear**: To clear the current input.
    - **Equals (=)**: To evaluate the expression.

## Script Breakdown

- **Imports**: 
    - `tkinter` for GUI components
    - `tkinter.messagebox` for error messages
    - `math` for mathematical operations

- **Main Window Setup**:
    - `window` to initialize the main window
    - `frame` to hold the calculator interface

- **Entry Widget**:
    - `entry` for input and display of expressions and results

- **Button Functions**:
    - `myclick(number)`: Inserts a number or operator into the entry widget.
    - `equal()`: Evaluates the expression in the entry widget and displays the result.
    - `clear()`: Clears the entry widget.
    - `square_root()`: Calculates and displays the square root of the current input.
    - `percentage()`: Calculates and displays the percentage of the current input.
    - `sin()`, `cos()`, `tan()`: Calculate and display the sine, cosine, and tangent of the current input (in degrees).

- **Buttons**:
    - Numerical buttons (0-9)
    - Arithmetic operation buttons (+, -, *, /)
    - Function buttons (sin, cos, tan, ^, %)
    - Control buttons (clear, =)

## Error Handling

- The script uses `try-except` blocks to handle invalid inputs and displays appropriate error messages using `tkinter.messagebox`.

## License

This project is licensed under the MIT License.


