import os
import datetime
os.system('cls')

# Prompts the user to enter a date in the format 'dd/mm/yyyy'.
input_date = input('Enter the date: dd/mm/yyyy: ')
date_format = '%d/%m/%Y'
try:
    datetime.datetime.strptime(input_date, date_format)  
except ValueError:
    print("Incorrect date format, should be dd/mm/yyyy")
    
day, month, year = input_date.split('/')
day = int(day)
month = int(month)
year = int(year)

if month < 1 or month > 12:
    print("Invalid month")
elif day < 1 or day > 31:
    print("Invalid day")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if day < 1 or day > 29:
            print("Invalid day for February in a leap year") 
    else:
        if day < 1 or day > 28:
            print("Invalid day for February")
elif month in [4, 6, 9, 11]:
    if day < 1 or day > 30:
        print("Invalid day")
else:
    print("Date is valid")


def year(date):
    return int(date[6:10])
def month(date):
    return int(date[0:2])
def day(date):
    return int(date[3:5])

print(f'Calculating for Day:{day(input_date)} Month:{month(input_date)} Year:{year(input_date)} ')