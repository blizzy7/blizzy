# Implement exact_calculator(left, operator, right). 
# Convert left and right to numbers. 
# Support addition, subtraction, multiplication, division, remainder, and exponent. 
# If either number cannot be converted, return Invalid number. 
# If the operator is not supported, return Invalid operator. 
# If division or remainder uses zero on the right side, return Cannot divide by zero. 
# Round numeric results to 2 decimal places.


def exact_calculator(left, operator, right):
    # Try to convert left and right to numbers
    try:
        left = float(left)
        right = float(right)
    except ValueError:
        return "Invalid number"

    # Check if the operator is supported
    if operator not in ['+', '-', '*', '/', '%', '**']:
        return "Invalid operator"

    # Perform the calculation based on the operator
    if operator == '+':
        result = left + right
    elif operator == '-':
        result = left - right
    elif operator == '*':
        result = left * right
    elif operator == '/':
        if right == 0:
            return "Cannot divide by zero"
        result = left / right
    elif operator == '%':
        if right == 0:
            return "Cannot divide by zero"
        result = left % right
    elif operator == '**':
        result = left ** right

    # Round the result to 2 decimal places
    return round(result, 2)