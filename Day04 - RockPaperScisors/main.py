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
options = [rock, paper, scissors]

player_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors."))
computer_picked = random.randint(0,2)
print(options[player_hand])
print("Computer chose:")
print(options[computer_picked])

if player_hand == computer_picked:
    print("Draw")
elif player_hand == 0 and computer_picked == 2 or \
        player_hand == 2 and computer_picked == 1 or \
        player_hand == 1 and computer_picked == 0:
    print("You won")
else:
    print("You lose")
