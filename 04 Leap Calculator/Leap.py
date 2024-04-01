import datetime

while True:
    
    userInput = input("Enter your Date of Birth in (dd/mm/yyyy) format: ")
    
    try:
        date_validator = datetime.datetime.strptime(userInput, '%d/%m/%Y')
        print("Valid date format.")
        
        # check if the mentioned date is a leap year or not
        if date_validator.year % 4 == 0:
            print("The mentioned date is a leap year.")
        else:
            print("The mentioned date is not a leap year.")
        
        break
    
    except:
        print("Invalid date format. \nPlease enter date in (dd/mm/yyyy) format.")