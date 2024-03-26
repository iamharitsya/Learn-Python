import os 
def welcome():
    os.system('cls')
    from Art import logo
    print(logo) 
    print('Welcome to the Auction\n\n')

log = {}
auction = True
while auction:
    
    welcome() # This function is called to print the logo and welcome message.
        
    bidder_name = input('Enter your name: ')      
    bidder_bid = int(input('Enter your bid: ₹ '))
    
    log[bidder_name] = bidder_bid
    
    print(f'\nThank you {bidder_name}, you have bid ₹ {bidder_bid}')
    

    next_person = input('Are there other bidders? (y/n)\n').lower()
    
    if next_person != 'y':
        
        auction = False # This is the condition to stop the loop.
        
        print(f'\nThe winner is {max(log, key=log.get)} with a bid of ₹ {max(log.values())}\n\n')