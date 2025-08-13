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

def enternewemployee():
        global NEXT_DRIVER_NUM
        Employee_ID = NEXT_DRIVER_NUM
        First_Name = input("Enter the employee first name: ").upper()
        Last_Name = input("Enter the employee last name: ").upper()
        Street_Add = input("Enter the employee street address: ")
        Phone = input("Enter the employee phone number[(XXX) XXX-XXXX]: ")
        formatted_phone = FV.format_phone(Phone)
        
        # Driver's license number entry.
        
        Driver_Lic_Num = input("Enter the driver's license number: ")
        Driver_Ex_Date = input("Enter the driver's expiry date (YYYY-MM-DD): ")
        
        # Balance due.
        BalDue = 0

        # Statement to determine if the license is valid or not.
        Driver_Ex_Date = datetime.datetime.strptime(Driver_Ex_Date, "%Y-%m-%d") # Year / month / day of the expiration date.
        
        if datetime.datetime.now() > Driver_Ex_Date:
            print("The driver's license is expired.") 
            exit()
        
        # Insurance information to be entered by the user and whether or not they are using their own vehicle.
            
        Ins_Comp = input("What is the name of the insurance company?: ").upper()
        Pol_Num = int(input("Enter the policy number for the driver: "))
        Own_Vehicle = input("Does the driver own his own vehicle? (Y/N): ").upper()
    
        # Append the information to the employees data file for storage.
        with open("Employees.dat", "a") as f:
            f.write(f"{Employee_ID}, {First_Name}, {Last_Name}, {Street_Add}, {formatted_phone}, {Driver_Lic_Num}, {Driver_Ex_Date}, {Ins_Comp}, {Pol_Num}, {Own_Vehicle}, {BalDue}\n")

        # Adds one number to the driver number each time a new employee is entered.
        NEXT_DRIVER_NUM += 1
        
        with open("Default.dat", "w") as f:
            
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
                print("     Data Entry Error - Rental ID cannot be blank.")
                print()
            else:
                break

        while True:
            # Input and validation for driver number.
            print()
            DriverNum = input("Enter the driver number: ")
            if DriverNum == "":
                print()
                print("     Data Entry Error - Rental ID cannot be blank.")
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
                    print("     Data Entry Error - Rental date cannot be blank.")
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
        f.write(f"{str(DriverNum)}, ")
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


#--------------------
# Record Employee Pay 
#--------------------

def record_payment():
    #Recoriding a payment.. this will write to its own file
     while True:
        payment_num = input("Enter Your Payment ID: ").strip()
        if payment_num != "":
             break
        else:
             print("Date Entry Error - Cannot Be Blank")
                # these ifs are set up different but result should be same
     while True: # Input and validation for driver number.
        DriverNum = input("Enter the driver number: ").strip()
        if DriverNum != "":
             break
        print("Data Entry Error - Rental ID can not be blank.")
            # Reasoning
     while True:
        reason = input("Enter Reason For Payment ").strip()
        if reason != "":
            break
        print("Reason Cannot Be Blank! ")      
# Date used is today
            
     pay_date = FV.FDateS(datetime.datetime.now())        # Amount Here 

     while True:
        Pay_amt = input("Enter The Amount Going To Be Paid: ").strip()
        try:
            amount = float(Pay_amt)
            if amount > 0:
                break
            else:
                print("Data Error -- Amount Must be numeric ") # non positive num
        except ValueError:
         print("Value Error - Must Be Numeric") # this means not a number 
            # Method Of Pay Here 
     ValidMethod = {"CASH","DEBIT","VISA"}   # These are allowed inputs           
     while True: 
        method = input("Enter The Method Of PAyment (Cash/Debit/Visa)").strip().upper()
        if method in ValidMethod:
            break
        print("Data ENtry Ertror - Method must be Cash, Debit or Visa")
     methoddsp = method.title()
     Pay_amtDsp = FV.FDollar2(amount)
            # Writing to the payments .dat file here 

     with open("Payments.dat", "a") as f:
      f.write(f"{payment_num}, {DriverNum}, {pay_date}, {Pay_amtDsp}, {reason}. {methoddsp}\n")
            
 
        # =================
        # Display results.
        # =================
     print()
     print()
     print(f"----------------------------------------")
     print(f"             Employee Payment           ")
     print(f"----------------------------------------")
     print(f"Payment ID:                    {payment_num}")
     print()
     print(f"Driver Number:                  {NEXT_DRIVER_NUM}")
     print()
     print(f"Reason For Payment:            {reason}")
     print()
     print(f"Pay Date:                      {pay_date}")
     print(f"----------------------------------------")
     print(f"Pay Type:                      {methoddsp}")
     print(f"                               ---------")
     print(f"Pay Amount:                    {Pay_amtDsp}")
     print(f"                               ---------")
   
     print(f"-----------------------------------------")
     print(f"     Thank you from Habs Taxi Service    ")
     print(f"-----------------------------------------")
     print()
     print()

#--------------------
# Print Profit Listing
#---------------------

def Profitlisting():
# Main report processing starts here.
    while True:
        # Input and validation for rentail start date.
        print()
        try:
            StartDate = input("Enter the start date (YYYY-MM-DD): ")
            StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
            if  StartDate == "":
                print()
                print("     Data Entry Error - Start date cannot be blank.")
                print()
        except ValueError:
            print()
            print(" Data Entry Error - Start date is invalid.")
            print()
        else:
            break

    while True:
        # Input and validation for rentail start date.
        print()
        try:
            EndDate = input("Enter the end date (YYYY-MM-DD): ")
            EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
            if  EndDate == "":
                print()
                print("     Data Entry Error - End date cannot be blank.")
                print()
        except ValueError:
            print()
            print(" Data Entry Error - End date is invalid.")
            print()
        else:
            break

    StartDateDsp = FV.FDateS(StartDate)
    EndDateDsp = FV.FDateS(EndDate)

    # Generate report heading for the profit listing report.
    print()
    print(f"                         HAB TAXI SERVICE                        ")
    print()
    print(f"                          PROFIT LISTING                         ")
    print()
    print(f" Start Date:   {StartDateDsp} ")
    print(f" End Date:     {EndDateDsp} ")
    print(f"----------------------------------------------------------------------")
    print()
    print(f" Transaction     Transaction         Sub                       Total  ")
    print(f"   Number           Date            Total          HST         Amount ")
    print(f"----------------------------------------------------------------------")
    print()

    # Initialize counters and accumulators.
    TotAmtAcc = 0

    # Open the data file. Places the cursor at the start of the first record.
    f = open("Revenue.dat", "r")

    # Process each line (record) in the file in a loop.
    for RevenueRecord in f:
    
        # The following line reads the first record in the file and creates a list.
        RevenueLst = RevenueRecord.split(",")
        
        # Now grab the values from the list and assign to variables.
        # You may not need all the fields.
        TransNum = RevenueLst[0].strip()
        TransDate = RevenueLst[1].strip()
        TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
        SubTot = float(RevenueLst[4].strip())
        Hst = float(RevenueLst[5].strip())
        TotalAmount = float(RevenueLst[6].strip())

        # Perform required calculations.
        # if statement to determine the dates to be displayed.
        if TransDate >= StartDate and TransDate <= EndDate:
            TransDateDsp = FV.FDateS(TransDate)
            SubTotDsp = FV.FDollar2(SubTot)
            HstDsp = FV.FDollar2(Hst)
            TotalAmountDsp = FV.FDollar2(TotalAmount)

            # Display the detail line.
            print(f"    {TransNum:<3s}          {TransDateDsp}        {SubTotDsp:<6s}        {HstDsp:<6s}      {TotalAmountDsp:6<s}")

            # Update counters and accumulators.
            TotAmtAcc += TotalAmount

    TotAmtAccDsp = FV.FDollar2(TotAmtAcc)

    # Close the file.
    f.close()

    # Print summary data - counters and accumulators.
    print()
    print(f"----------------------------------------------------------------------")
    print(f"                                             Revenue Total: {TotAmtAccDsp:12s}")
    print(f"                                                           -----------")
    print()

    # Start of Expenses listing report.
    print()
    print(f"                          HAB TAXI SERVICE                          ")
    print()
    print(f"                          EXPENSES LISTING                          ")
    print()
    print(f" Start Date:   {StartDateDsp} ")
    print(f" End Date:     {EndDateDsp} ")
    print(f"-------------------------------------------------------------------")
    print()
    print(f" Invoice       Invoice           Sub                       Total ")
    print(f"  Number         Date           Total         HST          Amount")
    print(f"-------------------------------------------------------------------")
    print()

    ItemTotAcc = 0

    # Open the data file. Places the cursor at the start of the first record.
    f = open("Expenses.dat", "r")

    # Process each line (record) in the file in a loop.
    for ExpensesRecord in f:
    
        # The following line reads the first record in the file and creates a list.
        ExpensesLst = ExpensesRecord.split(",")
        
        # Now grab the values from the list and assign to variables.
        # You may not need all the fields.
        InvNum = ExpensesLst[0].strip()
        TransDate = ExpensesLst[1].strip()
        TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
        SubTot = float(ExpensesLst[8].strip())
        Hst = float(ExpensesLst[9].strip())
        ItemTotAmt = float(ExpensesLst[10].strip())

        # Perform required calculations.
        # If statement to determine the date 
        if TransDate >= StartDate and TransDate <= EndDate:
            TransDateDsp = FV.FDateS(TransDate)
            SubTotDsp = FV.FDollar2(SubTot)
            HstDsp = FV.FDollar2(Hst)
            ItemTotAmtDsp = FV.FDollar2(TotalAmount)

            # Display the detail line.
            print(f"  {InvNum:<5s}       {TransDateDsp}       {SubTotDsp:<10s}    {HstDsp:<10s}    {ItemTotAmtDsp:<10s}")

            # Update counters and accumulators.
            ItemTotAcc += ItemTotAmt

    ItemTotAccDsp = FV.FDollar2(ItemTotAcc)

    # Close the file.
    f.close()

    print()
    print(f"-------------------------------------------------------------------")
    print(f"                                         Expanses Total: {ItemTotAccDsp:<12s}")
    print(f"                                                        -----------")
    print()
    # Calculation to determine the profit or loss.
    ProfitLoss = TotAmtAcc - ItemTotAcc
    ProfitLossDsp = FV.FDollar2(ProfitLoss)
    print()
    print(f"                Revenue Total:  {TotAmtAccDsp:>12s}                 ")
    print() 
    print(f"                                    Less the                        ")
    print()
    print(f"                Expanses Total: {ItemTotAccDsp:>12s}                ")
    print(f"                                  -----------                       ")
    print(f"           Profit / Loss total: {ProfitLossDsp:>12s}                ")
    print()
    print()
    print(f"--------------------------------------------------------------------")


#--------------------
# Print Driver Finance 
#--------------------

def print_finance():
                #prompts for input regarding the driver number start and end date 
        emp_num = input("Enter Employee Number: ").strip()
                #These Inputs Will BE Used For Validaitons

        start_date = input("Enter The Start Date: ").strip()[:10]
        end_date = input("Enter The End Date: ").strip()[:10]

        emp_name = "Not Found"
                #Opens revenue.dat in read mode
        with open("Employees.dat", "r") as emp_file:
            for line in emp_file:
                parts = line.strip().split(",")
                if parts[0] == emp_num:
                    emp_name = parts[1] + " " + parts[2].strip()
                    break


        print()
        print("HAB Taxi Driver Finance Listing")
        print("--------------------------------")
        print(f"Employee Name: {emp_name}")
        print("--------------------------------")
        print(f"Driver Number: {emp_num}")
        print(f"From {start_date} to {end_date}")
        print("--------------------------------")



        #this starts the holding amount of the program to be 0, no value
        balduac = 0.0
      
        with open("Revenue.dat", "r") as f:
         data = f.readlines() # this will read the entire file as list
            

        # this variable is set up to catch any unwanted entries
        found_any = False

        #loop starts here
        #this will loop through each revenue entry in the dat file
        for line in data:
            #These are testing out clean up methods
            parts = [p.strip() for p in line.strip().split(",")]

            # if there is less tha n4 sections it wont be a valid entry
            if len(parts) < 7:
                continue
            

            #Setting up points for line targeting
            file_emp_num = parts[3] 
            file_date = parts[1][:10]
            desc = parts[2]
            amount = float(parts[6])


            #This is for checking lines that match the entered data
            #Also Including the date Start and ENd



            if file_emp_num == emp_num and start_date <= file_date <= end_date:
                #This prints out the line from the section
                print(f"{file_date} {desc} ${amount:>,.2f}")
                #This increments the total amount
                balduac += amount
                #Marking the section that will be flagged here
                found_any = True
        #this is statment was for a check on matching record, these validations have been staying at the end
        #if no flags it will print

        print()
        if found_any:
            print("--------------------------------")
            print(f"Total:      ${balduac:,.2f}")
        else:
            print("-No Records Found for Employee-")
        print()




#--------------------------
# Menu Picking Portion Here 
#--------------------------
   # def main():

while True:

    print("        Habs Taxi Services         ")
    print("      Company Services System      ")
    print()
    print("1.   Enter a New Employee (driver).") # done ! 
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
    elif choice == "3":
        # Link compnay expense function .. and so on ,,, must write to expense function 
        expenses_output()
    elif choice == "4":
        # Track company Rentals.
        Rentals()
    elif choice == "5":
        # Record Employee Payment.
        record_payment()
    elif choice == "6":
        # Print Company Profit Listing.
        Profitlisting()
    elif choice == "7":
        print_finance()
    elif choice == "8":
        print("Good Bye ... ")
        quit()

    print()
    print()
    print("Data Saving.", end="", flush=True)
    time.sleep(0.6)
    print(".", end="", flush=True)
    time.sleep(0.6)
    print(".", end="", flush=True)
    time.sleep(0.5)
    print(".", end="", flush=True)
    time.sleep(0.5)
    print("Saved!", flush=True)
    time.sleep(0.6)
    print("Data Saved !")
    print()
    print()

#--------------------
# Exit Program 
#--------------------

# The Program will use defaults.dat to store constant data. 

# There will be a sample data file created for faker data.