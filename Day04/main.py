import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]
user_choice = int(input("What to you choose? Type 0 for Rock (🪨), 1 for Paper (📄) or 2 for Scissors (✂️).\n"))

if user_choice < 0 or user_choice > 2:
    print("You chose an invalid option. You lose! 💀")
else:
    user_selection = game_options[user_choice]
    print(f"{user_selection}")

    print("Computer chose:")
    computer_selection = random.choice(game_options)
    print(computer_selection)

    if user_selection == computer_selection:
        print("It's a draw! 🤝")
    elif ((user_selection == rock and computer_selection == scissors)
          or (user_selection == paper and computer_selection == rock)
          or (user_selection == scissors and computer_selection == paper)):
        print("You win! 🏆")
    else:
        print("You lose! ❌")
