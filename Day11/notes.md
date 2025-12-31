# Day 11 - Blackjack Capstone Project

## Topics Covered

- **List Operations**: Working with dynamic lists
- **Random Module**: Generating random choices
- **Functions with Multiple Returns**: Functions returning different values based on conditions
- **While Loops**: Implementing game logic with loops
- **Conditional Logic**: Complex decision-making structures
- **Game Development**: Building a complete card game
- **Blackjack Rules**: Understanding and implementing game rules

## Key Concepts

### Random Card Dealing

```python
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Four 10s represent 10, Jack, Queen, King
    # 11 represents Ace (can be 1 or 11)
    card = random.choice(cards)
    return card
```

### Score Calculation with Ace Logic

```python
def calculate_score(cards):
    """Calculate score with special rules for Blackjack and Aces"""
    # Check for Blackjack (21 with 2 cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents Blackjack

    # Convert Ace from 11 to 1 if score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
```

### Game Comparison Logic

```python
def compare(user_score, computer_score):
    """Compare scores and determine winner"""
    # Handle all possible outcomes:
    # - Draw
    # - Blackjack wins
    # - Bust losses (over 21)
    # - Score comparison
```

## Project: Blackjack Game

### Description

Built a fully functional Blackjack (21) card game. The program:

1. Deals two cards each to player and computer
2. Shows player's cards and one computer card
3. Allows player to draw additional cards or pass
4. Computer draws cards automatically until score >= 17
5. Compares final scores and determines the winner
6. Allows replay of the game

### Blackjack Rules Implemented

- **Card Values**:

  - Number cards (2-10) are worth their face value
  - Face cards (Jack, Queen, King) are worth 10
  - Ace is worth 11, but can become 1 if score exceeds 21

- **Blackjack**: Getting 21 with only 2 cards (Ace + 10-value card)

- **Dealer Rules**: Computer must draw cards until score is 17 or higher

- **Winning Conditions**:
  - Blackjack beats a regular 21
  - Going over 21 is an automatic loss (bust)
  - Higher score wins if both under 21
  - Draw if scores are equal

### Features

- **ASCII Art Logo**: Visual appeal with Blackjack branding
- **Dynamic Card Drawing**: Player chooses when to hit or stand
- **Automatic Dealer Logic**: Computer follows casino rules
- **Ace Conversion**: Automatically converts Ace from 11 to 1 when needed
- **Clear Game State**: Shows current cards and scores
- **Replay Option**: Can play multiple games in one session
- **Screen Clearing**: Clears screen between games for better UX
- **Comprehensive Win/Loss Messages**: Different messages for all outcomes

### Game Flow

```python
1. Display logo
2. Deal 2 cards to player and computer
3. Show player's cards and score
4. Show only computer's first card
5. Ask player to hit (y) or stand (n)
6. Calculate final scores
7. Computer draws until score >= 17
8. Compare scores and determine winner
9. Display final hands and result
10. Ask to play again
```

### Implementation Highlights

- **Modular Functions**: Separate functions for dealing, calculating, and comparing
- **Score Representation**: Using 0 to represent Blackjack for easier comparison
- **List Manipulation**: Dynamically adding cards to hands
- **Game Loop**: While loops for both player decisions and computer draws
- **Edge Case Handling**: Proper handling of Blackjack, bust, and Ace conversion

## Lessons Learned

- Breaking down complex game logic into manageable functions
- Handling special cases (Blackjack, Ace conversion) with conditional logic
- Using sentinel values (0 for Blackjack) to simplify comparisons
- Implementing game AI (dealer rules) with while loops
- Creating an engaging user experience with clear feedback
- Importance of testing all possible game outcomes
