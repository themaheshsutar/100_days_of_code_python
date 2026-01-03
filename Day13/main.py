############### Debugging Practice ###############

# Debugging is the process of finding and fixing errors in your code.
# This file contains various debugging exercises to practice common error types.

print("Welcome to Day 13 - Debugging Practice!")
print("=" * 50)

# ==================== Exercise 1: Describe Problem ====================
# Problem: Function should print numbers 1 to 20, but it's not working correctly
# Debugging technique: Add print statements to understand the flow

def my_function():
    print("\n--- Exercise 1: Describe Problem ---")
    # Original buggy code:
    # for i in range(1, 20):
    #     if i == 20:
    #         print("You got it")
    
    # Fixed code with explanation:
    for i in range(1, 21):  # Changed to 21 because range is exclusive of end
        if i == 20:
            print("You got it")
    
    print("Debugging tip: range(1, 20) goes from 1 to 19, not 20!")

my_function()


# ==================== Exercise 2: Reproduce the Bug ====================
# Problem: Bug occurs randomly with certain inputs
# Debugging technique: Find the specific input that causes the error

def reproduce_bug():
    print("\n--- Exercise 2: Reproduce the Bug ---")
    from random import randint
    
    # Original buggy code:
    # dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    # dice_num = randint(1, 6)
    # print(dice_imgs[dice_num])
    
    # Fixed code:
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, 5)  # Changed to 0-5 because list indices start at 0
    print(f"Dice roll: {dice_imgs[dice_num]}")
    
    print("Debugging tip: List indices start at 0, not 1!")

reproduce_bug()


# ==================== Exercise 3: Play Computer ====================
# Problem: Logic error in the year calculation
# Debugging technique: Step through the code like a computer

def play_computer():
    print("\n--- Exercise 3: Play Computer ---")
    year = int(input("What's your year of birth? "))
    
    # Original buggy code:
    # if year > 1980 and year < 1994:
    #     print("You are a millennial.")
    # elif year > 1994:
    #     print("You are a Gen Z.")
    
    # Fixed code:
    if year > 1980 and year < 1994:
        print("You are a millennial.")
    elif year >= 1994:  # Changed to >= to include 1994
        print("You are a Gen Z.")
    else:
        print("You are from an earlier generation.")
    
    print("Debugging tip: Check boundary conditions carefully!")

# Uncomment to test:
# play_computer()


# ==================== Exercise 4: Fix the Errors ====================
# Problem: Multiple syntax and logical errors
# Debugging technique: Read error messages carefully

def fix_errors():
    print("\n--- Exercise 4: Fix the Errors ---")
    
    # Original buggy code:
    # age = input("How old are you?")
    # if age > 18:
    #     print("You can drive at age {age}.")
    
    # Fixed code:
    age = int(input("How old are you? "))  # Added int() conversion
    if age >= 18:  # Changed to >= for proper condition
        print(f"You can drive at age {age}.")  # Fixed f-string
    else:
        print(f"You need to wait {18 - age} more years.")
    
    print("Debugging tip: Read error messages - they tell you exactly what's wrong!")

# Uncomment to test:
# fix_errors()


# ==================== Exercise 5: Print is Your Friend ====================
# Problem: Word not being added to list correctly
# Debugging technique: Use print() to check variable values

def print_debugging():
    print("\n--- Exercise 5: Print is Your Friend ---")
    pages = 0
    word_per_page = 0
    
    # Get input
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Words per page: "))
    
    # Original buggy code:
    # total_words = pages * word_per_page
    # print(total_words)
    
    # Debug with print statements:
    print(f"Debug: pages = {pages}, word_per_page = {word_per_page}")
    total_words = pages * word_per_page
    print(f"Total words: {total_words}")
    
    print("Debugging tip: Print variables at each step to see where things go wrong!")

# Uncomment to test:
# print_debugging()


# ==================== Exercise 6: Use a Debugger ====================
# Problem: Function producing wrong output
# Debugging technique: Use VSCode debugger with breakpoints

def use_debugger():
    print("\n--- Exercise 6: Use a Debugger ---")
    
    def mutate(a_list):
        b_list = []
        for item in a_list:
            new_item = item * 2
            b_list.append(new_item)  # Fixed: was using wrong variable
        print(b_list)
    
    mutate([1, 2, 3, 5, 8, 13])
    
    print("Debugging tip: Use VSCode debugger to step through code line by line!")

use_debugger()


# ==================== Exercise 7: Take a Break ====================
# Problem: Fresh eyes method
# Debugging technique: Step away from the code

def take_break():
    print("\n--- Exercise 7: Take a Break ---")
    print("Sometimes the best debugging technique is to:")
    print("1. Take a break ☕")
    print("2. Go for a walk 🚶")
    print("3. Come back with fresh eyes 👀")
    print("4. The bug often becomes obvious!")

take_break()


# ==================== Exercise 8: Ask a Friend ====================
# Problem: Rubber duck debugging
# Debugging technique: Explain code to someone (or something)

def ask_friend():
    print("\n--- Exercise 8: Ask a Friend/Rubber Duck ---")
    print("Explain your code line by line to:")
    print("• A colleague 👥")
    print("• A rubber duck 🦆")
    print("• A pet 🐕")
    print("Often you'll find the bug while explaining!")

ask_friend()


# ==================== Exercise 9: Run Often ====================
# Problem: Large blocks of unrun code accumulate bugs
# Debugging technique: Run code frequently as you write

def run_often():
    print("\n--- Exercise 9: Run Often ---")
    print("Don't write 100 lines before running!")
    print("✅ Write a few lines → Run → Test → Repeat")
    print("❌ Write everything → Run → Find 50 bugs")

run_often()


# ==================== Exercise 10: Ask StackOverflow ====================
# Problem: Stuck on an error you can't solve
# Debugging technique: Search for help online

def stack_overflow():
    print("\n--- Exercise 10: Search for Help ---")
    print("When stuck, try:")
    print("1. Copy the error message")
    print("2. Search on Google/StackOverflow")
    print("3. Read documentation")
    print("4. Check GitHub issues")
    print("Someone has probably solved this before!")

stack_overflow()


print("\n" + "=" * 50)
print("Debugging practice complete! Remember:")
print("🐛 Bugs are a normal part of coding")
print("🔍 Debugging is a skill that improves with practice")
print("💪 Every bug you fix makes you a better programmer")
