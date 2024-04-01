import os
os.system('cls')

import random
from art import cards, jack, welcome

print(jack)
print(welcome)

randomise = random.randint(1,13)

def shuffle(user,random_number):
    
    receive = random_number
    if user < 11 and receive == 1:
        value = 11
    elif receive > 10:
        value = 10
    else:
        value = receive
    return value

bank = 1000
   
while bank > 0:

    dealer  = 0
    dealer_set  = []
    
    gambler = 0
    gambler_set = []
    
    user_bet = int(input(f"\nCurrent Balance: {bank} \nHow much do you want to bet? [200/100/50]: ₹"))
    
    if user_bet not in [200, 100, 50]:
            print("Invalid bet. Please enter 200, 100 or 50.")
            continue
    if user_bet > bank:
        print(f"You don't have enough money to bet that much. \nAccount Balance ₹{bank}.\n\n")
        continue
    
    
    
    while dealer < 17: # Dealer bet 
    
        gen_random = random.randint(1,13)
        dealer_set.append(gen_random)        
        bet_value = shuffle(dealer, gen_random)
        dealer += bet_value
    
    print(f"\n\nDealer's first card: {cards[dealer_set[0]]}")
    
    
    
    while gambler < 21: # User bet
        
        gen_random = random.randint(1,13)
        gambler_set.append(gen_random)
        bet_value = shuffle(gambler, gen_random)
        gambler += bet_value
        
        print(f"Your card is: {cards[gen_random]} \n\nCurrent set: {gambler_set} \nSet value: {gambler}")
        
        if gambler > 21:
            bank -= user_bet
            print(f"Your set exceeds 21. 'You lose'\n\nDealer's total is ₹{dealer}. \nDealer's cards: {dealer_set}")
            print(f"Account Balance ₹{bank}.\n\n")
            break
        
        wish = input("Do you want to draw another card? [y/n]: ").lower()
            
        if wish not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        if wish == 'n':
            print(f"Your total is ₹{gambler}. Dealer's total is ₹{dealer}. \nDealer's cards: {dealer_set}")
            if dealer == gambler:
                print("Draw.")
                print(f"Account Balance ₹{bank}.\n\n")
                break
            elif dealer > gambler and dealer <= 21:
                print("You lose.")
                bank -= user_bet
                print(f"Account Balance ₹{bank}.\n\n")
                break
            else:
                print("You win.")
                bank += user_bet
                print(f"Account Balance ₹{bank}.\n\n")
            break



    user_choice = input("Do you want to play again? [y/n]: ").lower()
    if user_choice not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
    if user_choice!= 'y':
        print("Thanks for playing.")
        break
    
    if bank <= 0:
        print("You don't have enough money to play. Thanks for playing.")
        break