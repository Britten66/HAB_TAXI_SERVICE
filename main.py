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

    # Enter new Employee function.

    def enternewemployee():
        Employee_ID = input("Enter the employee ID: ")
        First_Name = input("Enter the employee first name: ").upper()
        Last_Name = input("Enter the employee last name: ").upper()
        Street_Add = input("Enter the employee street address:")
        Phone = input("Enter the employee phone number[(XXX) XXX-XXXX]: ")
        formatted_phone = FV.format_phone.format(Phone)
        
        # Employee information.
        Driver_Num = int(input("Enter the driver number: "))
    # Start checking this section here! 
        Driver_Ex_Date = FV.FDateS.format(2028, 12, 20) #Year / month / day of the expiration date.


        Driver_Ex_Date = FV.date(2028, 12, 20) # Year / month / day of the expiration date.
        if datetime.today() > Driver_Ex_Date:
            print("The driver's license is expired.") 
            exit()
    # Check this section for improvement!
            
        Ins_Comp = input("What is the name of the insurance company?: ").upper()
        Pol_Num = int(input("Enter the policy number for the driver: "))
        Own_Vehicle = input("Does the driver own his own vehicle? (Y/N): ").upper()
        
        with open("Employees.dat", "a") as f:
            f.write(f"{Employee_ID},{First_Name},{Last_Name},{Street_Add},{formatted_phone},{Driver_Num},{Driver_Ex_Date},{Ins_Comp},{Pol_Num},{Own_Vehicle}\n")
                        
#--------------------
# Track Car Rental 
#--------------------
        # Rental vehicle number for the user to select.
        Rental_Vehicle_Num = [1, 2, 3, 4]
        Rent_Period = ["day", "week"]

        if Own_Vehicle == "Y":
            print("Driver's vehicle used.")
            
        else:
            # Ask the user for rental details.
            Rent_Choice = int(input("Enter a vehicle rental number (1-4): "))
            Rent_Period = input("How long does the driver need the rental? (day / week): ").upper()
            if Rent_Choice in [1, 2, 3, 4]:
                print(f"Rental vehicle number {Rent_Choice} selected.")
            else:
                print("Invalid rental vehicle number.")

            if Rent_Period == "DAY":
                print('Rental period set to daily.')
            elif Rent_Period == "WEEK":
                print("Rental period set to weekly.")
            else:
                print("Invalid rental period.")

#--------------------
# Record Employee Pay 
#--------------------

#--------------------
# Print Profit Listing
#--------------------

#--------------------
# Menu Picking Portion Here 
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
# Print Driver Finance 
#--------------------

#--------------------
# Exit Program 
#--------------------

# The Program will use defaults.dat to store constant data. 

# There will be a sample data file created for faker data.