import random
from re import L
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

game_img = [rock,paper,scissors];

user_choice = int(input("What do you chosce? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >=3 or user_choice <0 :
    print("You typed an inwalid no. You Loss!!")
print(game_img[user_choice]);

computer_choice = random.randint(0,2);
print("computer choise")
print(game_img[computer_choice]);


if user_choice >=3 or user_choice <0 :
    print("You typed an inwalid no. You Loss!!")
    
elif user_choice == 0 and computer_choice == 2:
    print("You Win!!");
elif computer_choice == 0 and user_choice == 2:
    print("You Loss!!")
elif user_choice>computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!");
elif computer_choice == user_choice:
    print("Its a draw");
    

    