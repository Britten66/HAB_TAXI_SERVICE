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
        NEXT_TRANS_NUM = file.readlines() # 143 is the default driver number.
        NEXT_DRIVER_NUM = file.readlines() # 1922 is the default driver number.
        MONTHLY_STAND_FEE = file.readlines() # $175.00 for monthly stand fee for drivers with their own vehicle.
        DAILY_RENT_FEE = file.readlines() # $60.00 for daily fee.
        WEEKLY_RENT_FEE = file.readlines() # $300.00 for the weekly rent fee.
        HST_ESP = file.readlines() # 0.15 for HST rate.


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
            print("2.   Enter Company Revenues. ") # this is the problem we ran into with qap 4 -- 
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


# To do : 
    if choice == "1":
        FV.enternewemployee()
    elif choice == "2":
        # Link Company revenue function here function tto printt out a table and so on ,,, must write to revenue function 

    elif choice == "3":
        # Link expense here
        # Link compnay expense function .. and so on ,,, must write to expense function 

    elif choice == "4":

        # Track company Rentals.

    elif choice == "5":
        # Record Employee Payment.
    elif choice == "6":
        # Print Company Profit Listing.
    elif choice == "7":
        # Print Driver Financial Listing.
    elif choice == "8":
                   
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

# There will be a sample data file created for faker data.