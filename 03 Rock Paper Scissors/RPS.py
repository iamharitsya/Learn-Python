import random

from Art import you_win
from Art import welcome

print(f'{welcome} \nWelcome, remember “Rock breaks scissors, scissors cut paper, and paper covers rock.”')

while True:
  
  choices = ['rock', 'paper', 'scissors']
  comp_choice = random.choice(choices)
  
  while True:
    user_choice = input("\nI wish you good luck, choose your option (rock, paper, scissors):").lower()
    if user_choice in choices:
      break
    else:
      print("Invalid choice. Please enter rock, paper, or scissors.")
  
  print(f"Computer choose {comp_choice}\n")
  
  if user_choice == comp_choice:
    print("It's a tie!")
  
  elif user_choice == "rock":
    if comp_choice == "paper":
      print("You lose! Paper covers rock!")
    else:
      print("You win! Rock smashes scissors!")
      print(you_win)
  elif user_choice == "paper":
    if comp_choice == "scissors":
      print("You lose! Scissors cut paper!")
    else:
      print("You win! Paper covers rock!")
      print(you_win)  
  elif user_choice == "scissors":
    if comp_choice == "rock":
      print("You lose! Rock smashes scissors!")
    else:
      print("You win! Scissors cut paper!")
      print(you_win)
  
  conti = input("\n\nDo you want to play again? (y/n)\n").lower()
  
  if conti != 'y':
    print("\n\nThanks for playing!")
    break