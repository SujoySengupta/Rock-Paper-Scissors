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

#Write your code below this line 👇

import random
Hand_signs = [rock, paper, scissors]
choices = ['rock', 'paper', 'scissors']

user_input = input("Enter your choice (Rock, Paper, or Scissors):\n").lower()
user_choice_index = choices.index(user_input)

print(f"You chose {user_input.upper()}!\n{Hand_signs[user_choice_index]}")

computer_choice_index = random.randint(0, 2)
computer_sign = Hand_signs[computer_choice_index]
print(f"The computer chose {choices[computer_choice_index].upper()}!\n{computer_sign}")

if computer_sign == Hand_signs[user_choice_index]:
    print("It's a tie.")
else:
    if (user_choice_index == 0 and computer_choice_index == 2) or \
       (user_choice_index == 1 and computer_choice_index == 0) or \
       (user_choice_index == 2 and computer_choice_index == 1):
        print("You win!")
    else:
        print("You lose.")