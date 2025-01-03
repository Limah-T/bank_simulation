import random, os, datetime, json
from email_validator import validate_email, EmailNotValidError

# Create user account with the following requirements
class Create_User_Account:
    def __init__(self, fname, lname, middlename, gender, date_of_birth, next_of_kin, email, residential_address, phonenumber, state_of_origin, nationality, next_of_kin_rel):
        self.firstname = fname
        self.lastname = lname
        self.middlename = middlename
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.next_of_kin = next_of_kin
        self.email = email
        self.residential_address = residential_address
        self.phonenumber = phonenumber
        self.state_of_origin = state_of_origin
        self.nationality = nationality
        self.next_of_kin_rel = next_of_kin_rel
        self.all_account_numbers = []
        self.user_acct_to_shuffle = []
        self.user_acct_num = ""
        self.user_details = {}
        self.user_4_digits_pin = None
        self.user_balance = 0


    # Generate account number for user and make sure two users don't have same number
    def generate_account_number(self):
        looping = True
        while looping:
            for num in range(10):
                self.user_acct_to_shuffle.append(num)
            random.shuffle(self.user_acct_to_shuffle)
            for x in self.user_acct_to_shuffle:
                self.user_acct_num += str(x)
            if self.user_acct_num not in self.all_account_numbers:
                self.all_account_numbers.append((self.user_acct_num))
                looping = False
                return self.all_account_numbers
            else:
                looping = True
                
    
    def user_pin(self):
        """Prompt user for 4 digits pin twice and makes sure it matches"""
        looping = True
        while looping:
            try:
                pin1 = int(input("Create 4 digits pin for transactions: "))
                if len(str(pin1)) == 4:
                    pin2 = int(input("Retype 4 digits pin: "))
                else:
                    raise IndexError
            except ValueError:
                print("Only numbers are allowed")
                looping = True
            except IndexError:
                print("Pin must be length of 4")
                looping = True
                
            else:
                if pin1 == pin2:
                    self.user_4_digits_pin = int(pin1)
                    print("Pin created successfully")
                    looping = False
                else:
                    print("Pin do not match!")
                    looping = True
        if not looping:
            return True
   
    
    # Creates user account with valid information and account number added
    def user_account_creation(self):
        self.user_details[int(self.user_acct_num)] = [self.firstname, self.lastname, self.middlename, self.gender, self.date_of_birth, self.email, int(self.phonenumber), self.residential_address, self.state_of_origin, self.nationality, self.next_of_kin, self.next_of_kin_rel, float(self.user_balance), int(self.user_4_digits_pin)]

    # Checking user validily with account number and pin
    def validate_user_details(self):
        looping = True
        while looping:
            try:
                account_num = int(input("Enter your 10 digits account number: "))
                for valid_acct in self.user_details: 
                    if account_num == valid_acct:
                        pin = int(input("Enter your 4 digits pin: "))
                        if pin == self.user_details[valid_acct][-1]:
                            print("You are valid!")
                            looping = False
                            return account_num
                        else:
                            looping = True
                            raise KeyError
                    
                if account_num not in self.user_details:
                    looping = True
                    raise ValueError
            except ValueError:
                print("Invalid account number!")
            except KeyError:
                print("Incorrect pin for the provided account number!")
        if not looping:
            return True
        
            
    # Checking user balance after accurate validation process
    def check_balance(self, account_num):
        for valid_acct in self.user_details: 
            if account_num == valid_acct:      
                print(f"Account Number: {account_num}")
                print(f"Account Balance: #{self.user_details[valid_acct][-2]}")
                break

    # Deposit user money
    def deposit(self, account_num):
        print("Type ammount in numbers only without any characters or symbols")
        looping = True
        for valid_acct in self.user_details: 
            if account_num == valid_acct:
                while looping:
                    try:
                        depo = int(input("How much money do you want to deposit? "))
                        self.user_details[valid_acct][-2] += float(depo)
                        print(f"Available balance is now: #{self.user_details[valid_acct][-2]}")
                        print("Thank you for banking with us 🤝")
                        print(user.user_details)
                        break
                    except ValueError:
                        print("Type ammount in numbers only without any characters or symbols")
        if not looping:
            return True
        
        

    # Withdraw money from user balance if money is enough
    def withdraw(self, account_num):
        print("Type ammount in numbers only without any characters or symbols")
        looping = True
        for valid_acct in self.user_details: 
            if account_num == valid_acct:
                while looping:
                    try:
                        withdraw_money = float(input("How much money do you want to withdraw? "))
                        if self.user_details[valid_acct][-2] > withdraw_money:
                            self.user_details[valid_acct][-2] -= withdraw_money
                            print(f"Available balance is now: #{self.user_details[valid_acct][-2]}")
                            print("Thank you for banking with us 🤝")
                            looping = False
                        else:
                            print("Insufficient money to withdraw")
                            print(f"Available Balance: #{self.user_details[valid_acct][-2]}")
                            looping = True
                    
                    except ValueError:
                        print("Type ammount in numbers only without any characters or symbols")
                        looping = True
        if not looping:
            return True
       
        
    # Check user biography
    def biography(self, account_num):
        for valid_acct in self.user_details:
            if account_num == valid_acct:
                print("FirstName: ", self.user_details[valid_acct][0])
                print("LastName: ", self.user_details[valid_acct][1])
                print("MiddleName: ", self.user_details[valid_acct][2])
                print("Gender: ", self.user_details[valid_acct][3])
                print("Age: ", self.user_details[valid_acct][4])
                print("Email Address: ", self.user_details[valid_acct][5])
                print("Phone Number: ",self.user_details[valid_acct][6])
                print("Residential Address: ", self.user_details[valid_acct][7])
                print("State of Origin: ", self.user_details[valid_acct][8])
                print("Nationality: ", self.user_details[valid_acct][9])
                print("Next of Kin: ", self.user_details[valid_acct][10])
                print("Next of Kin Relationship: ", self.user_details[valid_acct][11])
                print("Account Number: ", account_num)
                print("Available Balance: #", self.user_details[valid_acct][-2])
                break


    # Make sure date of birth is properly formatted
    def check_date_of_birth(self):
        looping = True
        while looping:
            dob = input("Date of Birth(e.g 07/12/1990): ")
            split_dob = dob.split("/")
            try:
                splitted = f"{split_dob[0]}-{split_dob[1]}-{split_dob[2]}"
                self.date_of_birth = datetime.datetime.strptime(splitted, "%d-%m-%Y")
                looping = False
                return self.date_of_birth
            except IndexError:
                print("Enter the date of birth in this format e.g 07/12/1990")
                looping = True
            except ValueError:
                print(f"{dob} does not match this format e.g 07/08/1990")
        if not looping:
            return True
        
                
            
    # Make sure phone number consists of digit and not more than 11
    def check_phone_number(self):
        looping = True
        while looping:
            try:
                phone_number = int(input("Phone Number e.g 09012345678: "))
                if len(str(phone_number)) == 10:
                    self.phonenumber = phone_number
                    looping = False
                    return self.phonenumber
                else:
                    raise IndexError
            except ValueError:
                print("Only numbers are allowed!")
                looping = True
            except IndexError:
                print("Numbers must not be more than 11 digits")
                looping = True
        if not looping:
            return True
        

    # Asks for user operations
    def user_operation():
        choice = input("Type 'C' for create an account, 'D' for deposit, 'W' for withdraw, 'B' to check balance, 'X' to check biography, 'exit' to exit: ")
        return choice
            
    # Os function to clear screen 
    def clear_screen():
        os.system("cls")

        
        
# Asks user for their account number
print("Hello, Welcome to Finance your money ATM! 🤝")
is_atm_machine_on = True
no_error = True
no_phone_error = True
user = Create_User_Account(fname="", lname="", middlename="", gender="", date_of_birth="", next_of_kin="", email="", residential_address="", phonenumber="", state_of_origin="", nationality="", next_of_kin_rel="")
while is_atm_machine_on: 
    choice = Create_User_Account.user_operation() 
    match choice:
        case "C" | "c":
            firstname = input("FirstName: ").capitalize()
            lastname = input("LastName: ").capitalize()
            middlename = input("MiddleName: ").capitalize()
            gender = input("Gender: ").capitalize()
            if firstname != "" and lastname != "" and middlename != "" and gender != "":
                next_of_kin = input("Next of Kin: ").capitalize()
                next_of_kin_rel = input("Next of KIn Relationship: ").lower()
                state_of_origin = input("State of origin: ").capitalize()
                nationality = input("Nationality: ").capitalize()
                residential_add = input("Residential Address: ").capitalize()
                email = input("Email Address: ").lower()
                if next_of_kin != "" and next_of_kin_rel != "" and state_of_origin != "" and nationality != "" and residential_add != "" and email != "":
                        user = Create_User_Account(fname=firstname, lname=lastname, middlename=middlename, gender=gender, date_of_birth="", next_of_kin=next_of_kin, email=email, residential_address=residential_add, phonenumber="", state_of_origin=state_of_origin, nationality=nationality, next_of_kin_rel=next_of_kin_rel)
                        
                        birth_date = user.check_date_of_birth()
                        if birth_date:
                            call_number = user.check_phone_number()
                            if call_number:
                                user.date_of_birth = birth_date
                                user.phonenumber = call_number   
                                # Make sure user have the correct pin before showing the account number generated.
                                if user.user_pin():
                                    user.generate_account_number()
                                    user.user_account_creation()
                                    print(f"Account created successfully!\nHere is your account number {user.user_acct_num}\nAccount balance: #{user.user_balance}\nMake sure you save your details for future transactions.")
                                    print(user.user_details)
                        

            else:
                user.clear_screen() 
                print("Do not leave any detail blank!")    
                
        case "D" | "d":
            valid_user = user.validate_user_details()
            if valid_user:
                user.deposit(account_num=valid_user)
        
        case "W" | "w":
            valid_user = user.validate_user_details()
            if valid_user:
                user.withdraw(account_num=valid_user)
        
        case "B" | "b":
            valid_user = user.validate_user_details()
            if valid_user:
                user.check_balance(account_num=valid_user)
        
        case "X" | "x":
            valid_user = user.validate_user_details()
            if valid_user:
                user.biography(account_num=valid_user)

        case "Exit" | "exit":
            print("Bye!")
            break

        case _:
            print("Invalid input")
            user.clear_screen()
