# Day 10 - Functions with Outputs

## Topics Covered

- **Functions with Return Values**: Creating functions that output results
- **Return Statement**: Using `return` to send data back from functions
- **Recursion**: Functions calling themselves
- **Docstrings**: Documenting function purpose and behavior
- **Dictionary as Function Map**: Using dictionaries to store and call functions
- **Program Flow Control**: Managing loops and conditional logic

## Key Concepts

### Functions with Outputs

```python
# Function without return (returns None by default)
def greet(name):
    print(f"Hello {name}")

# Function with return value
def add(n1, n2):
    return n1 + n2

# Using the returned value
result = add(5, 3)
print(result)  # 8
```

### Multiple Return Paths

```python
def format_name(first, last):
    if first == "" or last == "":
        return "Invalid input"
    formatted = f"{first.title()} {last.title()}"
    return formatted
```

### Early Returns

Functions can have multiple return statements and exit early based on conditions:

```python
def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2
```

### Dictionary of Functions

Functions can be stored in dictionaries and called dynamically:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Call a function from the dictionary
result = operations["+"](5, 3)  # Calls add(5, 3)
```

### Recursion

A function can call itself, creating a recursive pattern:

```python
def calculator():
    # ... calculator logic ...
    if user_wants_new_calculation:
        calculator()  # Recursive call
```

**Note**: Be careful with recursion to avoid infinite loops. Always have a base case or exit condition.

## Project: Calculator

### Description

Built a fully functional calculator that performs basic arithmetic operations. The program:

1. Takes a first number as input
2. Displays available operations (+, -, *, /)
3. Takes the operator and second number
4. Calculates and displays the result
5. Allows user to continue with the result or start fresh
6. Uses recursion to restart calculations

### Features

- **Four Operations**: Addition, subtraction, multiplication, and division
- **Continuous Calculation**: Can use previous result for next calculation
- **Input Validation**: Checks for invalid operations
- **Recursive Restart**: Can start new calculations without exiting
- **Clean Interface**: ASCII art logo and screen clearing
- **Float Support**: Handles decimal numbers

### Implementation Highlights

#### Arithmetic Functions

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

#### Operations Dictionary

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

#### Calculator Logic

```python
def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    
    while should_accumulate:
        # Display operations
        for symbol in operations:
            print(symbol)
        
        operator = input("Pick an operation: ")
        
        # Validate operation
        if operator not in operations:
            print("Invalid operation.")
            continue
        
        num2 = float(input("What's the next number?: "))
        
        # Calculate result using dictionary lookup
        result = operations[operator](num1, num2)
        
        print(f"{num1} {operator} {num2} = {result}")
        
        # Continue or restart
        choice = input(f"Type 'y' to continue with {result}, 'n' to start new: ")
        
        if choice == "y":
            num1 = result  # Accumulate result
        else:
            should_accumulate = False
            calculator()  # Recursive call
```

## Key Takeaways

1. **Functions should do one thing well**: Each arithmetic function has a single, clear purpose
2. **Return values make functions reusable**: The result can be stored, displayed, or used in further calculations
3. **Dictionaries can map strings to functions**: Enables dynamic function calls based on user input
4. **Recursion is powerful but use carefully**: Good for restarting programs, but needs proper exit conditions
5. **Input validation improves user experience**: Checking for invalid operations prevents crashes
6. **Accumulator pattern**: Using previous results for continuous calculations

## Challenges Faced

- Deciding between recursion and loops for restart functionality
- Handling invalid operator input gracefully
- Managing the flow between continuing with result vs. starting fresh
- Screen clearing for better UI (platform-specific)

## Improvements for Future

- Add more operations (power, modulo, square root)
- Implement operation history
- Add error handling for division by zero
- Support for more complex expressions
- Save calculation history to file
