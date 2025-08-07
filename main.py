#Date: 08-04-2025
#Author(s): Robot Group 3

#Description: This Program simulates operations of HAB taxi services, 
#the program will allow the user to intereact with the company menu system.

#--------------------
# Imports Here
#--------------------
import time
import datetime
import FormatValues as FV

# Define program constents.
CURR_DATE = datetime.datetime.now()


while True:
    with open('Default.dat', 'r') as file:
        NEXT_TRANS_NUM = file.readlines()
        NEXT_DRIVER_NUM = file.readlines()
        MONTHLY_STAND_FEE = file.readlines() #For Drivers with their own vehicle.
        DAILY_RENT_FEE = file.readlines() #For drivers that rent one of the company cars.
        WEEKLY_RENT_FEE = file.readlines() # " "


# if Own_Vehicle == "Y":

# Bal_Due_Stand = 

#--------------------
# Main Function Will Be Here
#--------------------
    def main():
        while True:
            print("   HAB Taxi Services")
            print("Company Services System")
            print("1.   Enter a New Employee (driver). ")
            print("2.   Enter Company Revenues. ")
            print("3.   Enter Company Expenses. ")
            print("4.   Track Car Rentals. ")
            print("5.   Record Employee Payment. ")
            print("6.   Print Company Profit Listing. ")
            print("7.   Print Driver Profit Listing. ")
            print("8.   Quit Program. ")
            print()
    choice = input("        Enter Choice (1-8)")


#--------------------
# Menu Picking Portion Here 
#--------------------
    if choice == "1":
        FV.enternewemploy()
    elif choice == "2":
        #Link Companby revenue function here 
    elif choice == "3":
        #Link compnay expense function .. and so on ,,, 
    
#--------------------
# Track Car Rental 
#--------------------


#--------------------
# Record Employee Pay 
#--------------------

#--------------------
# Print Profit Listing
#--------------------

#--------------------
# Print Driver Finance 
#--------------------

#--------------------
# Exit Program 
#--------------------

# The Program will use defaults.dat to store constant data. 

# There will be a sample data file created for faker data, 