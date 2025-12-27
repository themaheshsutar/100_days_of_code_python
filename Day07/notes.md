# Day 07 - Hangman Game

## Topics Covered

- Modules and Imports
- Lists and List Methods
- String Concatenation
- Control Flow (While Loops, If-Else)
- Game Logic Implementation
- User Input Validation
- ASCII Art in Programs

## Key Concepts

### Importing Modules

```python
import random
import hangman_art
import hangman_words

# Accessing items from imported modules
word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo
```

### Working with Lists

```python
# Choosing random items from a list
chosen_word = random.choice(word_list)

# Building a list to track guessed letters
correct_letters = []
correct_letters.append(guess)

# Checking if item is in a list
if guess in correct_letters:
    print("Already guessed!")
```

### String Building and Manipulation

```python
# Building a placeholder string
placeholder = ""
for position in range(word_length):
    placeholder += "_"

# Building display string based on guessed letters
display = ""
for letter in chosen_word:
    if letter in correct_letters:
        display += letter
    else:
        display += "_"
```

### Input Validation

```python
guess = input("Guess a letter: ").lower()

# Validate input
if len(guess) != 1 or not guess.isalpha():
    print("Please enter a single valid letter.")
    continue
```

## Project: Hangman Game

### Game Description

A classic word-guessing game where the player tries to guess a word one letter at a time. The player has 6 lives, losing one life for each incorrect guess.

### Game Features

1. **Random Word Selection**: Chooses a random word from a word list
2. **Visual Feedback**: Shows hangman stages as lives decrease
3. **Input Validation**: Ensures only single letters are accepted
4. **Duplicate Prevention**: Tracks already guessed letters
5. **Win/Loss Conditions**: Detects when player wins or runs out of lives

### Project Structure

The project is organized into three files:

1. **main.py**: Contains the main game logic
2. **hangman_art.py**: Contains ASCII art for the logo and hangman stages
3. **hangman_words.py**: Contains the list of words to guess

### Game Logic Flow

```python
# 1. Setup
lives = 6
game_over = False
correct_letters = []
chosen_word = random.choice(word_list)

# 2. Create placeholder
placeholder = "_" * len(chosen_word)

# 3. Main game loop
while not game_over:
    # Get and validate user input
    guess = input("Guess a letter: ").lower()

    # Check for duplicate guesses
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    # Build display string
    display = ""
    for letter in chosen_word:
        if letter == guess or letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Check if guess is wrong
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOSE")

    # Check if player won
    if "_" not in display:
        game_over = True
        print("YOU WIN")

    # Show hangman stage
    print(stages[lives])
```

### Key Game Mechanics

#### Lives System

- Player starts with 6 lives
- Loses 1 life for each incorrect guess
- Game ends when lives reach 0

#### Display Building

- Initially shows underscores for each letter
- Updates to show correctly guessed letters
- Preserves previously guessed letters

#### Win/Loss Detection

```python
# Win condition
if "_" not in display:
    game_over = True
    print("YOU WIN")

# Loss condition
if lives == 0:
    game_over = True
    print(f"IT WAS {chosen_word}! YOU LOSE")
```

## What I Learned

- How to organize a project into multiple modules for better code structure
- How to import and use custom modules in Python
- The importance of input validation in user-facing programs
- How to track game state using variables (lives, correct_letters, game_over)
- Using lists to store and check previously guessed letters
- Building strings dynamically based on conditions
- The `continue` statement to skip the rest of a loop iteration
- How to use ASCII art to enhance console applications
- Breaking down complex game logic into manageable steps
- Using boolean flags to control game flow

## Key Takeaways

- **Modular Programming**: Separating concerns (game logic, art, data) makes code more maintainable
- **User Experience**: Input validation and clear feedback improve the game experience
- **State Management**: Tracking game state (lives, guesses) is crucial for game logic
- **String Manipulation**: Building strings character by character is a powerful technique
- **List Membership**: Using `in` operator for efficient membership testing
- **Loop Control**: `continue` statement helps skip unnecessary iterations

## Challenges Faced and Solutions

1. **Preventing Duplicate Guesses**: Maintained a `correct_letters` list to track all guessed letters
2. **Preserving Guessed Letters**: Checked both current guess and previous correct letters when building display
3. **Input Validation**: Used `len()`, `isalpha()`, and string methods to ensure valid input
4. **Displaying Lives Count**: Used f-strings to dynamically show remaining lives

## Possible Enhancements

- Add difficulty levels (easy, medium, hard words)
- Include hints after a certain number of wrong guesses
- Add a scoring system based on remaining lives
- Allow playing multiple rounds and track win/loss statistics
- Add categories for words (animals, countries, etc.)
- Implement a timer for added challenge
