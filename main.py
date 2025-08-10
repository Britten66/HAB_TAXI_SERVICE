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
        NEXT_TRANS_NUM = int(file.readlines()) # 143 is the default driver number.
        NEXT_DRIVER_NUM = int(file.readlines()) # 1922 is the default driver number.
        MONTHLY_STAND_FEE = float(file.readlines()) # $175.00 for monthly stand fee for drivers with their own vehicle.
        DAILY_RENT_FEE = float(file.readlines()) # $60.00 for daily fee.
        WEEKLY_RENT_FEE = float(file.readlines()) # $300.00 for the weekly rent fee.
        HST_ESP = float(file.readlines())# 0.15 for HST rate.






    # Enter new Employee function.

    def enternewemployee():
        Employee_ID = NEXT_DRIVER_NUM
        First_Name = input("Enter the employee first name: ").upper()
        Last_Name = input("Enter the employee last name: ").upper()
        Street_Add = input("Enter the employee street address:")
        Phone = input("Enter the employee phone number[(XXX) XXX-XXXX]: ")
        formatted_phone = FV.format_phone(Phone)
        
        # Employee information.
        Driver_Lic_Num = input("Enter the driver's license number: ")
   
        # Start checking this section here! 
        Driver_Ex_Date = FV.FDateS.format(2028, 12, 20) #Year / month / day of the expiration date.


        Driver_Ex_Date = FV.date(2028, 12, 20) # Year / month / day of the expiration date.
        if datetime.today().date() > Driver_Ex_Date:
            print("The driver's license is expired.") 
            exit()
        # End at this section for improvement!
            
        Ins_Comp = input("What is the name of the insurance company?: ").upper()
        Pol_Num = int(input("Enter the policy number for the driver: "))
        Own_Vehicle = input("Does the driver own his own vehicle? (Y/N): ").upper()
    
    
        with open("Employees.dat", "a") as f:
            f.write(f"{Employee_ID}, {First_Name}, {Last_Name}, {Street_Add}, {formatted_phone}, {Driver_Lic_Num}, {Driver_Ex_Date}, {Ins_Comp}, {Pol_Num}, {Own_Vehicle}\n")

        NEXT_DRIVER_NUM += 1
        with open("Defaults.dat", "w") as f:
            
            f.write(f"{NEXT_TRANS_NUM}\n") 
            f.write(f"{NEXT_DRIVER_NUM}\n") 
            f.write(f"{MONTHLY_STAND_FEE }\n") 
            f.write(f"{DAILY_RENT_FEE }\n") 
            f.write(f"{WEEKLY_RENT_FEE }\n") 
            f.write(f"{HST_ESP}\n")
                            
#--------------------
# Track Car Rental 
#--------------------
    def Rentals():

        while True:
            # Input and validation for rentail ID.
            RentalID = input("Enter the rental ID: ")
            if RentalID == "":
                print()
                print("     Data Entry Error - Rental ID can not be blank.")
                print()
            else:
                break

        while True:
            # Input and validation for driver number.
            DriverNum = input("Enter the driver number: ")
            if DriverNum == "":
                print()
                print("     Data Entry Error - Rental ID can not be blank.")
                print()
            else:
                break

        while True:
            # Input and validation for rentail start date.
            try:
                RenStartDate = input("Enter the start date of the rental: ")
                RenStartDate = FV.FDateS(RenStartDate)
                if  RenStartDate == "":
                    print()
                    print("     Data Entry Error - Rental ID can not be blank.")
                    print()
            except ValueError:
                print()
                print(" Data Entry Error - The rental date is invalid.")
                print()
                continue
            else:
                break

        CarRentedLst = [1, 2, 3, 4]
        while True:
            # Input and validation for the car number rented.
            CarRented = input("Enter the car to be rented (1, 2, 3 or 4): ")
            CarRented = int(CarRented)
            if CarRented == "":
                print()
                print("     Data Entry Error - Car rented can not be blank.")
                print()
            elif CarRented not in CarRentedLst:
                print()
                print("     Data Entry Error - Car rented is invalid.")
                print()
            else:
                break

        while True:
            # Input and validation for the amount of days(s) the car will be rented.
            NumDaysRen = input("Enter the number of days you wnat to rent a car (Day or Week): ").title()
            if NumDaysRen == "":
                print()
                print("     Data Entry Error - Number of days rented can not be blank.")
                print()
            elif NumDaysRen.isalpha == False:
                print()
                print("     Data Entry Error - Number of day(s) rented must be either 'Day' (1 day) or 'Week' (7 days).")
                print()
            elif NumDaysRen == "Day":
                NumDaysRen = 1
            elif NumDaysRen == "Week":
                NumDaysRen = 7
            else:
                break

        # Statement and calculation for the rental cost.
        if CarRented in CarRentedLst == True and NumDaysRen == 1:
            RentalCost = DAILY_RENT_FEE * NumDaysRen
        elif CarRented in CarRentedLst == True and NumDaysRen == 7:
            RentalCost = WEEKLY_RENT_FEE * NumDaysRen

        # Calculation for the rental Hst.
        RentalHst = RentalCost * HST_ESP

        # Calculation for the rental total.
        TotRenCost = RentalCost + RentalHst

        # Display results.
        print()
        print()

        f = open("Rental.dat", "a") 
    
        f.write(f"{str(RentalID)}, ")
        f.write(f"{str(DriverNum)}, ")
        f.write(f"{str(RenStartDate)}, ")
        f.write(f"{str(NumDaysRen)}, ")
        f.write(f"{str(CarRented)}, ")
        f.write(f"{str(RentalCost)}, ")
        f.write(f"{str(RentalHst)}, ")
        f.write(f"{str(TotRenCost)}\n ")

        f.close

        f = open("Revenue.dat", "a")

        f.write(f"{str(NEXT_TRANS_NUM)}, ")
        f.write(f"{str(FV.FDateS(CURR_DATE))}, ")
        f.write(f"Car Rental Cost", )
        f.write(f"{str(DriverNum)}", )
        f.write(f"{str(RentalCost)}", )
        f.write(f"{str(RentalHst)}", )
        f.write(f"{str(TotRenCost)}\n")

        f.close()

        NEXT_TRANS_NUM += 1

        f = open("Default.dat", "w")

        f.write(f"{NEXT_TRANS_NUM}\n") 
        f.write(f"{NEXT_DRIVER_NUM}\n") 
        f.write(f"{MONTHLY_STAND_FEE }\n") 
        f.write(f"{DAILY_RENT_FEE }\n") 
        f.write(f"{WEEKLY_RENT_FEE }\n") 
        f.write(f"{HST_ESP}\n")

        f.close()

        '''
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
            '''

                


#--------------------
# Record Employee Pay 
#--------------------

    def record_payment()
    #Recoriding a payment.. this will write to its own file

    while True:
        payment_num = input("Enter Your Payment ID: ").strip()
        if payment_num != "":
            break
        else: ValueError
        print("Date Entry Error - Cannot Be Blank")
 # these ifs are set up different but result should be same
    while True:
        # Input and validation for driver number.
        DriverNum = input("Enter the driver number: ").strip()
        if DriverNum == "":
            print()
            print("     Data Entry Error - Rental ID can not be blank.")
            print()
        else:
            break

    while True:
        reason = input("Enter Reason For Payment ").strip()
        if reason == "":
            print()
            print("         Data Entry Error")      

#--------------------
# Date used is today
#--------------------
 
        pay_date = datetime.now() 
    
#--------------------
# Amount Here 
#--------------------

        while True:
         Pay_amt = input("Enter The Amount Going To Be Paid: ").strip()
         try:
            amount = float(Pay_amt)
            if amount > 0:
                break
            print("Data Error -- Amount Must be numeric ") # non positive num

         except ValueError:
          print("Data Enbtrey Eror") # this means not a number 

#--------------------
# Method Of Pay Here 
#--------------------
       
        ValidMethod = {"CASH","DEBIT","VISA"}   # These are allowed inputs 
        while True: 
            method = input("Enter The Method Of PAyment (Cash/Debit/Visa)").strip().upper()
            if method in ValidMethod:
                break
            print("Data ENtry Ertror - Method must be Cash, Debit or Visa")
            
        methoddsp = method.title()

#--------------------
# Writing to the payments .dat file here 
#--------------------

        with open("Payments.dat", "a") as f:
         f.write(f"{payment_num}, {DriverNum}, {pay_date}, {amount:.2f}, {reason}. {methoddsp}\n")





#--------------------
# Print Profit Listing
#--------------------
    Emp_ID = enternewemployee() # Used to get the employee ID from the function. 
   
#   Calculations to be made.
    TransactionID = 0 #As we don't know the ID number or alpha numerical code for this, I set it to 0.
    TransAmt = 0.00 #Enter calculation here!
    HSTAmt = TransAmt * HST_ESP
    TotalAmt = TransAmt + HSTAmt
    # Minus off of the Expenses, such as the repairs, expenses and office ID's to get the total amount.

    
    with open("Finance.dat", "w") as f:
          f.write(f"{Emp_ID}, {TransactionID}, {TransAmt}, {HSTAmt}, {TotalAmt}\n")
          
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
        enternewemployee()
    elif choice == "2":
        # Link Company revenue function here function tto printt out a table and so on ,,, must write to revenue function 
        print(f"Choice 2")
    elif choice == "3":
        # Link expense here
        # Link compnay expense function .. and so on ,,, must write to expense function 
        print(f"Choice 3")
    elif choice == "4":
        # Track company Rentals.
        Rentals()
    elif choice == "5":
        # Record Employee Payment.
        print(f"Choice 5")
    elif choice == "6":
        # Print Company Profit Listing.
        print(f"Profit Listing")
    elif choice == "7":
        # Print Driver Financial Listing.
        print(f"Diver Finacial Listing")
    elif choice == "8":
        quit()

#--------------------
# Print Driver Finance 
#--------------------

#--------------------
# Exit Program 
#--------------------

# The Program will use defaults.dat to store constant data. 

# There will be a sample data file created for faker data.