# Day 06 - Functions, Code Blocks, and While Loops

## Topics Covered

- Functions (Built-in and User-defined)
- Function Parameters
- While Loops
- Code Blocks and Indentation
- Problem-solving with Algorithms

## Key Concepts

### Defining Functions

```python
def my_function():
    # Code block
    print("Hello from function")

# Calling the function
my_function()
```

### While Loops

```python
while condition:
    # Code runs as long as condition is True
    do_something()
```

The while loop continues executing the code block until the condition becomes False.

### Code Blocks

- Code blocks are defined by indentation in Python
- Functions and loops contain code blocks
- Indentation must be consistent (usually 4 spaces)

## Project: Reeborg's World - Maze Challenge

### Problem

Navigate a robot through a maze to reach the goal using functions and while loops.

### Solution Strategy

The solution uses the **right-hand wall following algorithm**:
1. If the right side is clear, turn right and move
2. Else if the front is clear, move forward
3. Else turn left

This algorithm guarantees finding the exit in mazes with connected walls.

### Key Functions Used

```python
def turn_right():
    # Turn right by turning left three times
    turn_left()
    turn_left()
    turn_left()

def follow_right_wall():
    # Implements the right-hand rule
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

### Main Algorithm

```python
# Initial positioning
while front_is_clear():
    move()
turn_left()

# Maze solving loop
while not at_goal():
    follow_right_wall()
```

## What I Learned

- How to define custom functions to organize code
- How to reuse functions to avoid repetition (DRY - Don't Repeat Yourself)
- How while loops work with conditions
- The difference between for loops (iterate a set number of times) and while loops (iterate until condition is False)
- How to break down complex problems into smaller functions
- The right-hand wall following algorithm for maze solving
- The importance of proper indentation in Python

## Notes

- **While loops** are useful when you don't know how many iterations are needed in advance
- **Functions** help organize code into reusable blocks
- The `turn_right()` function is built from `turn_left()` because Reeborg can only turn left by default
- The right-hand rule works for simply-connected mazes (mazes where all walls are connected)
- Always ensure while loops have a condition that will eventually become False to avoid infinite loops

## Reeborg's World

- Platform: https://reeborg.ca/reeborg.html
- A great tool for learning programming logic and problem-solving
- Provides visual feedback for code execution
- Helps understand functions and loops in a practical way
