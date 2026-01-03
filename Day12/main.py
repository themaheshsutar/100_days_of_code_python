import art
import random

# Constants for game configuration
MIN = 1
MAX = 100
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """Sets the number of turns based on user input."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, secret_number, turns):
    """Checks guess against the secret number and returns the remaining turns."""
    if guess > secret_number:
        print("Too high.")
        return turns - 1
    elif guess < secret_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {secret_number}.")
        return 0  # Using 0 to signal the game is won


def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN} and {MAX}.")

    secret_number = random.randint(MIN, MAX)
    turns = set_difficulty()

    guess = 0
    while guess != secret_number:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Get user input and handle basic range validation
        guess = int(input("Make a guess: "))

        if guess < MIN or guess > MAX:
            print(f"Please stay within the range {MIN} to {MAX}.")
            continue

        turns = check_answer(guess, secret_number, turns)

        if turns == 0 and guess != secret_number:
            print(f"You've run out of guesses! The number was {secret_number}. Better luck next time!")
            break
        elif guess == secret_number:
            break


play_game()