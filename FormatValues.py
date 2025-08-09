# Library of functions for formatting numbers and dates.

import datetime

#Receipt Generator Function

def Receipt_gen_id(FirstName, LastName, Plate, Phone):
      if len(Phone) == 10 and Phone.isdigit():
        Initials = FirstName[0].upper() + LastName[0].upper()
        LastThree = Plate[-3:]
        LastFour = Phone[-4:]
        return(f"{Initials}-{LastThree}-{LastFour}")
      else:
       print("Phone Number Is invalid. Please try again")
      exit()

#Here is current Date 

CURRENT_DATE = datetime.datetime.now() 

def first_payment_date():
    one_month = datetime.timedelta(days=30)
    return (CURRENT_DATE + one_month).strftime("%b %d, %Y")

#Format Phone Function

def format_phone(Phone):

    area = Phone[0:3]
    middle = Phone[3:6]
    end = Phone[6:10]
    return "(" + area + ")" + middle + "-" + end 

# Enter new Employee function.

def enternewemployee():
    Employee_ID = input("Enter the employee ID: ")

    First_Name = input("Enter the employee first name: ").upper()
    Last_Name = input("Enter the employee last name: ").upper()
    Street_Add = input("Enter the employee street address:")
    Phone = input("Enter the employee phone number[(XXX) XXX-XXXX]: ")
    formatted_phone = format_phone.format(Phone)
    
    # Employee information.
    Driver_Num = int(input("Enter the driver number: "))
    Driver_Ex_Date = FDateS.format(2028, 12, 20) #Year / month / day of the expiration date.
   
   
    if datetime.today() > Driver_Ex_Date:
        print("The driver's license is expired.") 
        exit()
     
    Ins_Comp = input("What is the name of the insurance company?: ").upper()
    Pol_Num = int(input("Enter the policy number for the driver: "))
    Own_Vehicle = input("Does the driver own his own vehicle? (Y/N): ").upper()
    
    # Rental vehicle number for the user to select.
    Rental_Vehicle_Num = [1, 2, 3, 4]
    Rent_period = ["day", "week"]

    if Own_Vehicle == "Y":
        print("Driver's vehicle used.")
        
    elif Rent_Choice == input("Enter a vehicle rental number(1-4): "):
         Rent_Choice = int(Rental_Vehicle_Num)
    elif Rent_period == input("How long does the driver need the rental? (please choose  day / week): ").upper():
        Rent_period = Rent_period

    else: 
        print("Invalid number selection, Please choose a number between 1 and 4.")

    

        
# How to split up 2 outputs from a funciton
# def get_name_parts(full_name):
#      first, last = full_name.split()
#      return first, last

# fname, lname = get_name_parts("")
# print(fname)  
# print(lname)  



#Mileage Function

def mileage_valid(mileage_input):
    try:
         mileage = int(mileage_input)
         if mileage >= 0:
            return mileage
         else:
            print("Mileage must be greater than zero ")
    except ValueError:
        print("Mileage Must Be Whole Number")
            
   

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to #,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to #,###.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to ####.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to ####.#.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to ####.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr
