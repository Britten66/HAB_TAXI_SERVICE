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
import os 

# Define program constents.
CURR_DATE = datetime.datetime.now()


with open('Default.dat', 'r') as f:
    NEXT_TRANS_NUM = int(f.readline()) # 143 is the default driver number.
    NEXT_DRIVER_NUM = int(f.readline()) # 1922 is the default driver number.
    MONTHLY_STAND_FEE = float(f.readline()) # $175.00 for monthly stand fee for drivers with their own vehicle.
    DAILY_RENT_FEE = float(f.readline()) # $60.00 for daily fee.
    WEEKLY_RENT_FEE = float(f.readline()) # $300.00 for the weekly rent fee.
    HST_ESP = float(f.readline())# 0.15 for HST rate.



os.system("cls" if os.name == "nt" else "clear") # Clears the screen when program is lanched.

    # Enter new Employee function.
while True: 

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
# Revenue Here
#--------------------
    def revenue_output():

     with open('Revenue.dat', 'r') as f:
        REV_OUTPUT = str(f.readlines()) # will print revenue file list
     
        print(f"{REV_OUTPUT}")

#--------------------
# Expenses Here
#--------------------
    def expenses_output():
 
     with open('Expenses.dat', 'r') as f:
        EXP_OUTPUT = str(f.readlines()) # will print expense file list

        print(f"{EXP_OUTPUT}")



#--------------------
# Track Car Rental 
#--------------------
    def Rentals():

        f = open('Default.dat', 'r')

        NEXT_TRANS_NUM = int(f.readline()) # 143 is the default driver number.
        NEXT_DRIVER_NUM = int(f.readline()) # 1922 is the default driver number.
        MONTHLY_STAND_FEE = float(f.readline()) # $175.00 for monthly stand fee for drivers with their own vehicle.
        DAILY_RENT_FEE = float(f.readline()) # $60.00 for daily fee.
        WEEKLY_RENT_FEE = float(f.readline()) # $300.00 for the weekly rent fee.
        HST_ESP = float(f.readline())# 0.15 for HST rate.

        f.close()

        while True:
            # Input and validation for rentail ID.
            print()
            RentalID = input("Enter the rental ID: ")
            if RentalID == "":
                print()
                print("     Data Entry Error - Rental ID can not be blank.")
                print()
            else:
                break

        while True:
            # Input and validation for driver number.
            print()
            DriverNum = input("Enter the driver number: ")
            if DriverNum == "":
                print()
                print("     Data Entry Error - Rental ID can not be blank.")
                print()
            else:
                break

        while True:
            # Input and validation for rentail start date.
            print()
            try:
                RenStartDate = input("Enter the start date of the rental (YYYY-MM-DD): ")
                RenStartDate = datetime.datetime.strptime(RenStartDate, "%Y-%m-%d")
                if  RenStartDate == "":
                    print()
                    print("     Data Entry Error - Rental date can not be blank.")
                    print()
            except ValueError:
                print()
                print(" Data Entry Error - The rental date is invalid.")
                print()
                
            else:
                break


        while True:
            # Input and validation for the car number rented.
            print()
            CarRented = input("Enter the car to be rented (1, 2, 3 or 4): ")
            CarRented = int(CarRented)
            if CarRented > 4:
                print()
                print("  Data Entry Error - Must Be a Valid Number Between 1-4. ")
                print()
            elif CarRented <= 0:
                print()
                print("  Data Entry Error - Must Be a Valid Number Between 1-4.")
                print()
            else:
                break

        while True:
            # Input and validation for the amount of days(s) the car will be rented.
            print()
            NumDaysRen = input("Rental Choice - (Day/Week): ").title()
            if NumDaysRen == "":
                print()
                print("     Data Entry Error - Number of days rented can not be blank.")
                print()
            elif NumDaysRen.isalpha == False:
                print()
                print("     Data Entry Error - Number of day(s) rented must be either 'Day' (1 day) or 'Week' (7 days).")
                print()
            else:
                break

                # Validation for num days rented via day/week 
        if NumDaysRen == "Day":
            NumDaysRen = 1
        elif NumDaysRen == "Week":
            NumDaysRen = 7

        # Statement and calculation for the rental cost.
        NumDaysRen = int(NumDaysRen)
        if NumDaysRen == 1:
            RentalCost = DAILY_RENT_FEE
        elif NumDaysRen == 7:
            RentalCost = WEEKLY_RENT_FEE

        RentalCostDsp = FV.FDollar2(RentalCost)

        # Calculation for the rental Hst.
        RentalHst = RentalCost * HST_ESP
        RentalHstDsp = FV.FDollar2(RentalHst)

        # Calculation for the rental total.
        TotRenCost = RentalCost + RentalHst
        TotRenCostDsp = FV.FDollar2(TotRenCost)

        CURR_DATEDsp = FV.FDateM(CURR_DATE)

        RenStartDateDsp = FV.FDateM(RenStartDate)

        # Display results.
        print()
        print()
        print(f"----------------------------------------")
        print(f"             Rental Receipt             ")
        print(f"----------------------------------------")
        print(f" Rental ID:                      {RentalID:>6s} ")
        print()
        print(f" Diver Number:                  {DriverNum:>6s}")
        print()
        print(f" Car Rented:                     {CarRented:>2d}")
        print()
        print(f" Start Date of rental:        {RenStartDateDsp}")
        print(f"----------------------------------------")
        print(f" Number of days rented:          {NumDaysRen:>2d}")
        print(f"                               ---------")
        print(f" Rental Cost:                   {RentalCostDsp:>6s}")
        print()
        print(f" Hst:                            {RentalHstDsp:>6s}")
        print(f"                               ---------")
        print(f" Total Rental Cost:             {TotRenCostDsp:>6s}")
        print(f"-----------------------------------------")
        print(f" Rental requested on:          {CURR_DATEDsp}")
        print(f"-----------------------------------------")
        print(f"     Thank you from Habs Taxi Service    ")
        print(f"-----------------------------------------")
        print()
        print()


        f = open("Rental.dat", "a") 

        f.write(f"{str(RentalID)}, ")
        f.write(f"{str(DriverNum)}, ")
        f.write(f"{FV.FDateS(RenStartDate)}, ")
        f.write(f"{str(NumDaysRen)}, ")
        f.write(f"{str(CarRented)}, ")
        f.write(f"{str(RentalCost)}, ")
        f.write(f"{str(RentalHst)}, ")
        f.write(f"{str(TotRenCost)}\n ")

        f.close

        f = open("Revenue.dat", "a")

        f.write(f"{NEXT_TRANS_NUM}, ")
        f.write(f"{str(FV.FDateS(CURR_DATE))}, ")
        f.write(f"Car Rental Cost, ")
        f.write(f"{str(DriverNum)}")
        f.write(f"{str(RentalCost)}, ")
        f.write(f"{str(RentalHst)}, ")
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

    def record_payment():
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


# Date used is today

 
        pay_date = datetime.now() 
    

# Amount Here 


        while True:
         Pay_amt = input("Enter The Amount Going To Be Paid: ").strip()
         try:
            amount = float(Pay_amt)
            if amount > 0:
                break
            print("Data Error -- Amount Must be numeric ") # non positive num

         except ValueError:
          print("Data Enbtrey Eror") # this means not a number 


# Method Of Pay Here 

       
        ValidMethod = {"CASH","DEBIT","VISA"}   # These are allowed inputs 
        while True: 
            method = input("Enter The Method Of Payment (Cash/Debit/Visa)").strip().upper()
            if method in ValidMethod:
                break
            print("Data Entry Ertror - Method must be Cash, Debit or Visa")
            
        methoddsp = method.title()


# Writing to the payments .dat file here 

        with open("Payments.dat", "a") as f:
         f.write(f"{payment_num}, {DriverNum}, {pay_date}, {amount:.2f}, {reason}. {methoddsp}\n")
 




#---------------------
# Print Profit Listing
#---------------------







#--------------------------
# Menu Picking Portion Here 
#--------------------------
   # def main():

        #while True:

    print("        Habs Taxi Services         ")
    print("      Company Services System      ")
    print()
    print("1.   Enter a New Employee (driver). ") # done ! 
    print("2.   Enter Company Revenues. ") # this is the problem we ran into with qap 4 --  # Done ! 
    print("3.   Enter Company Expenses. ") # Done ! 
    print("4.   Track Car Rentals. ")
    print("5.   Record Employee Payment. ")
    print("6.   Print Company Profit Listing. ") 
    print("7.   Print Driver Profit Listing. ")
    print("8.   Quit Program. ")
    print()

    choice = input("     Enter Choice (1-8): ")


# To do : 
    if choice == "1":
        enternewemployee()
    elif choice == "2":
        # Link Company revenue function here function tto printt out a table and so on ,,, must write to revenue function 
        revenue_output()
        print(f"Choice 2")
    elif choice == "3":
        # Link compnay expense function .. and so on ,,, must write to expense function 
        expenses_output()
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
        print("Good Bye ... ")
        quit()

#--------------------
# Print Driver Finance 
#--------------------

#--------------------
# Exit Program 
#--------------------

# The Program will use defaults.dat to store constant data. 

# There will be a sample data file created for faker data.