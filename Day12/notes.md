# Day 12 - Scope & Number Guessing Game

## Topics Covered

- **Scope**: Understanding local, global, and block scope
- **Global vs Local Variables**: Difference between variable scopes
- **Constants**: Using uppercase naming for constant values
- **Functions with Return Values**: Functions returning different values based on logic
- **Game Loop Logic**: Implementing game flow with while loops
- **Input Validation**: Basic range checking for user input
- **Random Number Generation**: Using `random.randint()` for game logic

## Key Concepts

### Variable Scope

#### Local Scope

Variables defined inside a function exist only within that function:

```python
def my_function():
    local_var = 10  # Only accessible inside this function
    print(local_var)

my_function()
# print(local_var)  # This would cause an error
```

#### Global Scope

Variables defined outside all functions are accessible everywhere:

```python
global_var = 20  # Accessible everywhere

def my_function():
    print(global_var)  # Can read global variables

my_function()
print(global_var)  # Also accessible here
```

#### Block Scope

Python doesn't have block scope like some other languages. Variables in if/while/for blocks are accessible outside:

```python
if True:
    x = 10

print(x)  # This works in Python
```

### Constants

Use uppercase naming convention for constants (values that shouldn't change):

```python
MIN = 1
MAX = 100
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
```

**Note**: Python doesn't enforce constants, but the naming convention signals intent.

### Functions with Different Return Values

Functions can return different values based on conditions:

```python
def check_answer(guess, secret_number, turns):
    """Returns remaining turns or 0 if game is won"""
    if guess > secret_number:
        print("Too high.")
        return turns - 1
    elif guess < secret_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {secret_number}.")
        return 0  # Special value to signal win
```

### Game Loop with Exit Conditions

Using while loops with multiple exit conditions:

```python
while guess != secret_number:
    # Game logic

    if turns == 0 and guess != secret_number:
        # Out of turns - lose
        break
    elif guess == secret_number:
        # Correct guess - win
        break
```

## Project: Number Guessing Game

### Description

Built a number guessing game where the computer picks a random number and the player tries to guess it. The program:

1. Displays a welcome message with ASCII art
2. Randomly generates a number between 1 and 100
3. Asks player to choose difficulty (easy or hard)
4. Gives player limited attempts based on difficulty
5. Provides feedback on each guess (too high/too low)
6. Tracks remaining attempts
7. Validates that guesses are within range
8. Announces win or loss at the end

### Difficulty Levels

- **Easy Mode**: 10 attempts to guess the number
- **Hard Mode**: 5 attempts to guess the number

### Game Features

- **ASCII Art Logo**: Visual branding using custom ASCII art
- **Random Number Generation**: Secret number between 1-100
- **Difficulty Selection**: Player chooses easy or hard mode
- **Attempt Tracking**: Shows remaining guesses after each attempt
- **Input Validation**: Checks if guess is within valid range (1-100)
- **Feedback System**: Tells player if guess is too high or too low
- **Clear Win/Loss Messages**: Different messages for success and failure
- **Constants**: Clean code using named constants for game configuration

### Game Flow

1. **Initialization**

   - Display logo and welcome message
   - Generate random secret number
   - Get difficulty level from player
   - Set number of turns based on difficulty

2. **Game Loop**

   - Display remaining attempts
   - Get player's guess
   - Validate guess is in range (1-100)
   - Check if guess is correct, too high, or too low
   - Update remaining turns
   - Continue until player guesses correctly or runs out of turns

3. **End Game**
   - If correct: Congratulate player
   - If out of turns: Reveal the secret number

### Code Organization

The program is organized into clear functions:

- `set_difficulty()`: Handles difficulty selection and returns turn count
- `check_answer()`: Compares guess to secret number and returns updated turns
- `play_game()`: Main game logic coordinating all components

### Key Learning Points

1. **Scope Management**: Functions use local variables while accessing global constants
2. **Return Values**: Functions return values that update game state
3. **Clean Code**: Constants at top, descriptive function names, clear docstrings
4. **Game State**: Using return values to track and update game progress
5. **User Experience**: Clear prompts, feedback, and range validation

## Best Practices Applied

- **Constants in UPPERCASE**: `MIN`, `MAX`, `EASY_LEVEL_TURNS`, `HARD_LEVEL_TURNS`
- **Descriptive Function Names**: `set_difficulty()`, `check_answer()`, `play_game()`
- **Docstrings**: Each function includes a description of its purpose
- **Separation of Concerns**: Each function has a single, clear responsibility
- **Input Validation**: Checking user input is within expected range
- **Clear Variable Names**: `secret_number`, `turns`, `guess` are self-explanatory
