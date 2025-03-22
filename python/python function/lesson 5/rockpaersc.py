import random

options = ["Rock","Paper","Scissors"]
user_choice = input("choose Rock,Paper, or Scissors: ")
computer_choice = random.choice(options)
print("your choice:",user_choice)
print("computer choice",computer_choice)
if user_choice==computer_choice:
    print('its a draw')
elif user_choice=="Rock" and computer_choice=="Scissors":
    print('rock wins')
elif user_choice=="Paper" and computer_choice=="Rock":
    print('Paper wins')
elif user_choice=="Scissors" and computer_choice=="Paper":
    print('Scissor wins')
else:
    print(' lose')
