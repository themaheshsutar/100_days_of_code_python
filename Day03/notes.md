# Day 03 - Conditional Statements and Control Flow

## Topic: Nested If/Else Statements

### Key Concepts Learned

1. **If/Elif/Else Statements**

   - `if` - executes code block if condition is true
   - `elif` - checks another condition if previous conditions were false
   - `else` - executes code block if all other conditions are false

2. **Nested Conditionals**

   - Placing if/else statements inside other if/else blocks
   - Creates branching decision paths
   - Useful for multi-level decision making

3. **Input Handling**

   - Using `input()` to get user input
   - Using `.lower()` to normalize input (case-insensitive comparison)
   - Type conversion and string methods

4. **Multi-line Strings**
   - Using `r'''...'''` for raw multi-line strings
   - Preserves formatting and special characters (like ASCII art)

### Code Structure

```python
# Example of nested conditionals
if condition1:
    # First level decision
    if condition2:
        # Second level decision
        if condition3:
            # Third level decision
            # action
```

### Project: Treasure Island Game

A text-based adventure game that demonstrates:

- Multiple choice decision making
- Nested conditional logic (3 levels deep)
- User input validation
- String manipulation
- ASCII art display

**Game Flow:**

1. Choose direction: left or right
2. If left → Choose action: wait or swim
3. If wait → Choose door: red, yellow, or blue
4. Only yellow door leads to winning

### Important Notes

- Always consider edge cases (invalid inputs)
- Indentation is crucial in Python for nested statements
- Each decision path should have a clear outcome
- Use meaningful variable names for readability
