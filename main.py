#Date: 08-04-2025
#Author(s): Robot Group 3

#Description: This Program simulates operations of HAB taxi services, 
#the program will allow the user to intereact with the company menu system.

#--------------------
# Imports Here
#--------------------

import datetime

try:
    with open('Default.dat', 'r') as file:
        NEXT_TRANS_NUM = file.read()
        NEXT_DRIVER_NUM = file.read()
        MONTHLY_STAND_FEE = file.read() #For Drivers with their own vehicle.
        DAILY_RENT_FEE = file.read() #For drivers that rent one of the company cars.
        WEEKLY_RENT_FEE = file.read() # " "

except FileNotFoundError:
    print("Error: Default.dat file not found.")

Employee_ID = input("Enter the employee ID: ")

First_Name = input("Enter the employee first name: ").upper()
Last_Name = input("Enter the employee last name: ").upper()
Street_Add = input("Enter the employee street address:")
Phone = input("Enter the employee phone number[(XXX) XXX-XXXX]: ")
formatted_phone = # Import Phone Function 


Driver_Num = int(input("Enter the driver number: "))
# Driver_Ex_Date = 
Ins_Comp = input("What is the name of the insurance company?: ").upper()
Pol_Num = int(input("Enter the policy number for the driver: "))
Own_Vehicle = input("Does the driver own his own vehicle? (Y/N): ").upper()


# if Own_Vehicle == "Y":

# Bal_Due_Stand = 

#--------------------
# Enter Company Revenue 
#--------------------

#--------------------
# Enter Company Expense 
#--------------------

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