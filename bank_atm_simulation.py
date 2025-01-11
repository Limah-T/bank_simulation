import random, os, datetime, json, re, csv
from email_validator import validate_email, EmailNotValidError
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()
print(load_dotenv())
token = os.environ.get('fernet_token')
json_filepath = os.environ.get('json_file_path')
json_beneficiary_filepath = os.environ.get('json_beneficiary_file_path')
csv_file_path = os.environ.get('csv_filepath')
key = Fernet(token)

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
        self.user_acct_to_shuffle = []
        self.user_acct_num = ""
        self.user_details = {}
        self.user_transaction_history = 0
        self.user_4_digits_pin = None
        self.user_balance = 0
        self.date_of_acct_created = datetime.datetime.now().date().strftime("%b %d, %Y"), datetime.datetime.now().strftime("%I:%M%p").lower()
        self.transaction_date = self.date_of_acct_created[0]
        self.transaction_time = self.date_of_acct_created[1]
        self.states_in_nigeria = [ "Abia state", "Adamawa state", "Akwaibom state", "Anambra state", "Bauchi state", "Bayelsa state", "Benue state", "Borno state", "Cross River state", "Delta state",
    "Ebonyi state", "Edo state", "Ekiti state", "Enugu state", "Gombe state", "Imo state", "Jigawa state", "Kaduna state", "Kano state", "Katsina state",
    "Kebbi state", "Kogi state", "Kwara state", "Lagos state", "Nasarawa state", "Niger state", "Ogun state", "Ondo state", "Osun state", "Oyo state",
    "Plateau state", "Rivers state", "Sokoto state", "Taraba state", "Yobe state", "Zamfara state"]
        self.load_json_file()

    # Asks the user for thier details with the each prompt message, remove trailing whitespaces, and replace spaces with no space, any character if added, prompt the user to input string not to be left empty.
    
    # Validate firstname input
    def get_valid_firstname(self):
        empty = True
        while empty:
            firstname = input("FirstName: ").capitalize().strip()
            fname = re.sub(r'[^a-zA-Z]', '', firstname)
            if fname:
                empty = False
            else:
                print("Firstname cannot be empty!")
        if not empty:
            return fname

    # Validate last name input  
    def get_valid_last_name(self):
        empty = True
        while empty:
            lastname = input("LastName: ").capitalize().strip()
            lname = re.sub(r'[^a-zA-Z]', '', lastname)
            if lname:
                empty = False
            else:
                print("Lastname cannot be empty!")
        if not empty:
            return lname

    # Validate middlename input 
    def get_valid_middlename(self):
        empty = True
        while empty:
            middlename = input("MiddleName: ").capitalize().strip()
            mname = re.sub(r'[^a-zA-Z]', '', middlename)
            if mname:
                empty = False
            else:
                print("Middlename cannot be empty!")
        if not empty:
            return mname

    # Validate gender input   
    def get_valid_gender(self):
        empty = True
        while empty:
            gender = input("Gender (Male/Female): ").capitalize().strip()
            gender_format = re.sub(r'[^a-zA-Z]', '', gender)
            match gender_format:
                case 'Male' |  'M' | 'Female' | 'F':
                    if gender_format == 'M' or gender_format == 'Male':
                        gender_format = 'Male'
                        confirm = True
                        empty = False
                    elif gender_format == 'F' or gender_format == 'Female':
                        gender_format = 'Female'
                        confirm = True
                        empty = False
                case " ":
                    print("Gender cannot be empty!")
                case _:
                    print("Invalid input!")        
        if confirm:
            return gender_format
        
    # Validate residential address input  
    def get_valid_residential_address(self):
        empty = True
        while empty:
            residential_add = input("Residential Address e.g ikoyi, lagos: ").capitalize().strip()
            residence_format = re.sub(r'[^a-zA-Z]+$', '', residential_add)
            if "," in residence_format:
                res = residence_format.split(",")
                first = res[0].capitalize()
                second = res[1].upper()
                residence = f"{first + ','}{second}"
                empty = False
            else:
                print("Input residence in this format e.g Ikoyi, Lagos and cannot be empty!")
        if not empty:
            return residence

    # Validate state of origin input      
    def get_valid_state_of_origin(self):
        empty = True
        while empty:
            state_of_origin = input("State of origin e.g Lagos, Abia, Kano, Port-Harcourt: ").capitalize().strip()
            state = re.sub(r'[^a-zA-Z-]+$', " ", state_of_origin)
            if state in self.states_in_nigeria:
                empty = False
            else:
                print("Input state of origin in the format e.g Kwara state, make user its part of Nigeria States, and cannot be empty!")
        if not empty:
            return state
        
    # Validate nationality inpput    
    def get_valid_nationality(self):
        empty = True
        while empty:
            nationality = input("Nationality (Enter Nigerian): ").capitalize().strip()
            nation = re.sub(r'[^a-zA-Z]', '', nationality)
            if nation and nation == "Nigerian":
                empty = False
            else:
                print("Invalid input, and Nationality cannot be empty!")
        if not empty:
            return nation
        
    #  Validate next of kin input  
    def get_valid_next_of_kin(self):
        empty = True
        while empty:
            next_of_kin = input("Next of Kin: ").capitalize().strip()
            nok = re.sub(r'[^a-zA-Z]', '', next_of_kin)
            if nok:
                empty = False
            else:
                print("Next of Kin cannot be empty!")

        if not empty:
            return nok

    # Validate next of kin relationship input
    def get_valid_next_of_kin_rel(self):
        empty = True
        while empty:
            next_of_kin_rel = input("Next of KIn Relationship: ").capitalize()
            nok_rel = re.sub(r'[^a-zA-Z]', '', next_of_kin_rel)
            if nok_rel:
                empty = False
            else:
                print("Next of kin relationship cannot be empty!")
        if not empty:
            return nok_rel
        

    # Check for email validation 
    def get_valid_email(self):
        email_error = True
        while email_error:
            self.email = input("Email Address: ").lower()
            try:
                email_is_valid = validate_email(self.email, check_deliverability=False)
                if email_is_valid:
                    if self.check_if_email_already_exist(new_email=self.email):
                        email_error = False
                        return self.email
                    else:
                        raise ValueError
            except EmailNotValidError:
                print("Invalid email address!")
            except ValueError:
                print(f"{self.email} already exist with a specific account, ERROR")
        if not email_error:
            return True
        
    def check_if_email_already_exist(self, new_email):
        user_details = self.load_json_file()
        exist = False
        if user_details:
            for email_exist in user_details:
                for x in email_exist:
                    if new_email in email_exist[x][0]:
                        exist = True
                    else:
                        exist = False
        if not exist:
            return True
        return False
                    

    # Make sure date of birth is properly formatted
    def get_valid_date_of_birth(self):
        looping = True
        while looping:
            dob = input("Date of Birth(e.g 07/12/1990): ")
            split_dob = dob.split("/")
            try:
                splitted = f"{split_dob[0]}/{split_dob[1]}/{split_dob[2]}"
                formatted_dob = datetime.datetime.strptime(splitted, "%d/%m/%Y")
                self.date_of_birth = datetime.datetime.strftime(formatted_dob.date(), "%d %b, %Y")
                looping = False
                return str(self.date_of_birth)
            except IndexError:
                print("Enter the date of birth in this format e.g 07/12/1990")
                looping = True
            except ValueError:
                print(f"{dob} does not match this format e.g 07/08/1990")
        if not looping:
            return True             
            
    # Make sure phone number consists of digit and not more than 11
    def get_valid_phone_number(self):
        looping = True
        while looping:
            try:
                phone_number = input("Phone Number e.g 09012345678: ")
                if phone_number.isdigit() and len(str(phone_number)) == 11:
                    self.phonenumber = phone_number
                    if self.check_if_phonenum_already_exist(phonenumber=phone_number):
                        looping = False
                        return self.phonenumber
                    else:
                        raise KeyError
                else:
                    raise IndexError
            except ValueError:
                print("Only numbers are allowed!")
                looping = True
            except IndexError:
                print("Numbers must not be more than 11 digits")
            except KeyError:
                print(f"{phone_number} already exist with a specific account, ERROR")
        if not looping:
            return True

    # Check if phone number already exist
    def check_if_phonenum_already_exist(self, phonenumber):
        user_details = self.load_json_file()
        exist = False
        if user_details:
            for email_exist in user_details:
                for x in email_exist:
                    if phonenumber in email_exist[x][0]:
                        exist = True
                    else:
                        exist = False
        if not exist:
            return True
        return False
    
    # Generate account number for user and make sure two users don't have same number
    def generate_account_number(self):
        looping = True
        while looping:
            for num in range(10):
                self.user_acct_to_shuffle.append(num)
            random.shuffle(self.user_acct_to_shuffle)
            for x in self.user_acct_to_shuffle:
                self.user_acct_num += str(x)
            user_details = self.load_json_file()
            if user_details != None:
                for double_acct_num in user_details:
                    if self.user_acct_num not in double_acct_num:
                        looping = False
                        return self.user_acct_num
                else:
                    looping = True
            else:
                return self.user_acct_num

          
    # Request for user pin, validate it to be integer, and re-confirm.
    def create_user_pin(self):
        """Prompt user for 4 digits pin twice and makes sure it matches"""
        looping = True
        while looping:     
            pin1 = input("Create 4 digits pin for transactions: ")
            try:
                pin_format1 = re.sub(r'[^0-9]', '', pin1)
                if pin_format1:
                    if pin1.isdigit() and len(pin1) == 4 :
                        pin2 = input("Retype 4 digits pin: ")
                        pin_format2 = re.sub(r'[^0-9]', '', pin2)
                        if pin_format1:
                            confirm = True
                        else:
                            raise ValueError    
                    else:
                        raise IndexError
                else:
                    raise ValueError
            except ValueError:
                print("Only numbers are allowed")
            except IndexError:
                print("Pin must be length of 4")
            else:               
                if pin_format1 == pin_format2:
                    self.user_4_digits_pin = pin_format1
                    print("Pin created successfully")
                    looping = False
                    encrypted_pin = self.encrypt_user_pin(string_pin=self.user_4_digits_pin)
                    return encrypted_pin
                else:
                    print("Pin do not match!")
            
        if not looping:
            return True
        

    # Harsh user's password for save security in Json using cryptography fernet
    def encrypt_user_pin(self, string_pin):
        change_pin_to_byte = key.encrypt(string_pin.encode("utf-8"))
        """JSON only accept string not byte as password"""
        string = change_pin_to_byte.decode("utf-8")
        return string
    
    # Decrypt user's pin from bytes back to string to enable comparison from what user input
    def decrypt_user_pin_bytes_to_string(self, string_pin2):
        """Fernet accepts bytes not string, so we decode the string to and pass to fernet to decrypt and give the original password"""
        change_byte = string_pin2.decode("utf-8")
        decode_pin = key.decrypt(change_byte).decode("utf-8")
        return decode_pin

    # Add user details to Json file.
    def add_user_details_to_json(self, user_details):
        try:
            with open(json_filepath, mode="r", encoding="utf-8") as file:
                json_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            json_data = []
        json_data.append(user_details)
        with open(json_filepath, mode="w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)
            file.write("\n")
                
    # Loads JSON file.
    def load_json_file(self):
        """If user is to perform any operation, it loads the json file, if true: proceed and checks for user validity, else: prompt the user massage for thier invalidity"""
        looping = True
        while looping:
            try:
                with open(json_filepath, mode="r", encoding="utf-8") as file:
                    json_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                break
            else:
                looping = False
                return json_data
        if not looping:
            return True
            
            
    # Asks user for account number  
    def ask_for_acct_num(self):
        """Asks user for account number, validate it to be integer, then check in json as str of account number cause json saves the account number which is the key as string"""
        looping = True
        while looping:
            try:
                account_num = int(input("Enter your 10 digits account number: "))
                if len(str(account_num)) == 10:
                    user_details = self.load_json_file()
                    if user_details:
                        for valid in user_details:
                            if str(account_num) in valid:
                                looping = False
                                return account_num
                        if looping:
                            raise KeyError
                    else:
                        print("Account is not valid, make sure you input the right account number!")
     
                else:
                    raise KeyError
            except ValueError:
                print("Only numbers are allowed!")
            except KeyError:
                print("Invalid account number")
            
        if not looping:
            return True

    # Ask user for pin   
    def ask_for_pin(self, account_num):
        """Asks for user pin, then validate it if it is thsame as what the user input when creating the account, else prompt user of invalid pin for the specified acct num"""
        looping = True
        while looping:
            try:
                pin = input("Enter your 4 digits pin: ")
                if pin.isdigit() and len(str(pin)) == 4:
                    user_details = self.load_json_file() 
                    string_format = f"{account_num}"
                    for valid in user_details:
                        if string_format in valid:
                            """Change saved password from Json string to byte"""
                            pin_encrypt = valid[string_format][0][-2].encode("utf-8")
                            pin_decrypt = self.decrypt_user_pin_bytes_to_string(string_pin2=pin_encrypt)
                            if pin_decrypt == pin:
                                looping = False
                            else:
                                raise KeyError
                else:
                    raise KeyError
            except ValueError:
                print("Only numbers are allowed!")
            except KeyError:
                print("Invalid pin input!")       
        if not looping:
            return True
    
    
    # Checking user validily with account number and pin
    def validate_user_details(self):
        """Checks for user's validity with account number provided and pin, if user input wrong pin
        3times, user's account get blocked for 20mins which has raised scam alert"""
        confirmed = False
        attempts = 3
        account_num = self.ask_for_acct_num()
        if account_num:
            pin = self.ask_for_pin(account_num=account_num)
            if pin:
                confirmed = True
                self.clear_screen()
                return account_num
        if confirmed:
            return True
        

    # Check user biography
    """Print out user's details only if the user is valid with the correct account num and pin (from validate method)"""
    def biography(self, account_num):
        user_details = self.load_json_file()
        string_format = str(account_num)
        self.clear_screen()
        for valid_acct in user_details:
            if string_format in valid_acct:
                print("FirstName: ", valid_acct[string_format][0][0])
                print("LastName: ", valid_acct[string_format][0][1])
                print("MiddleName: ", valid_acct[string_format][0][2])
                print("Gender: ", valid_acct[string_format][0][3])
                print("Age: ", valid_acct[string_format][0][4])
                print("Email Address: ", valid_acct[string_format][0][5])
                print("Phone Number: ", valid_acct[string_format][0][6])
                print("Residential Address: ", valid_acct[string_format][0][7])
                print("State of Origin: ", valid_acct[string_format][0][8])
                print("Nationality: ", valid_acct[string_format][0][9])
                print("Next of Kin: ", valid_acct[string_format][0][10])
                print("Next of Kin Relationship: ", valid_acct[string_format][0][11])
                print("Account Number: ", account_num)
                print("Available Balance: #", valid_acct[string_format][0][-3])
                break

             
    # Checking user balance after accurate validation process
    def check_balance(self, account_num):
        """Loads the json and check for print user's balance only if the user is valid (from validate user method)"""
        user_details = self.load_json_file()
        string_acct = str(account_num)
        for valid_acct in user_details: 
            if string_acct in valid_acct:
                self.clear_screen()      
                print(f"Account Number: {string_acct}")
                print(f"Account Balance: #{valid_acct[string_acct][0][-3]}")
                break   

    # Deposit user money
    def deposit(self, account_num):
        """Loads json file, verify valid user's details from(validate method),  """
        print("Type ammount in numbers only without any characters or symbols")
        user_details = self.load_json_file()
        string_format = str(account_num)
        for valid_acct in user_details:
            if string_format in valid_acct:    
                while True:
                    try:
                        depo = float(input("How much money do you want to deposit? "))
                        print(string_format, type(string_format))
                        if string_format in valid_acct:
                            print(True)
                            updated_bal = valid_acct[string_format][0][-3] + depo         
                            valid_acct[string_format][1].append(f"{self.date_of_acct_created[0]} {self.date_of_acct_created[1]}  {depo}     Credit (Deposited)")
                            transaction = valid_acct[string_format][1]
                            confirmed = True
                            break
                        print(False)
                    except ValueError:
                        print("Type ammount in numbers only without any characters or symbols")
        if confirmed:
            for valid in user_details:
                if string_format in valid:
                    valid[string_format][0][-3] = updated_bal
                    valid[string_format][1] = transaction
            with open(json_filepath, mode="w", encoding="utf-8") as file:
                json.dump(user_details, file, indent=4)
            self.clear_screen()
            print(f"Deposited {depo}")
            print(f"Available balance is now: #{valid_acct[str(account_num)][0][-3]}" )
            print("Thank you for banking with us 🤝")    

    # Withdraw money from user balance if money is enough
    def withdraw(self, account_num):
        print("Type ammount in numbers only without any characters or symbols")
        user_details = self.load_json_file()
        if user_details:
            string_format = str(account_num) 
            for valid_acct in user_details: 
                if string_format in valid_acct:
                    while True:
                        try:
                            withdraw_money = float(input("How much money do you want to withdraw? "))
                            if valid_acct[string_format][0][-3] > withdraw_money:
                                updated_bal = valid_acct[string_format][0][-3] - withdraw_money
                                valid_acct[string_format][0][-3] = updated_bal
                                valid_acct[string_format][1].append(f"{self.date_of_acct_created[0]} {self.date_of_acct_created[1]}  {withdraw_money}       Debit (Withdrew)")
                                transaction = valid_acct[string_format][1]
                                valid_acct[string_format][1] = transaction
                                self.clear_screen()
                                print(f"Withdrew {withdraw_money}")
                                print(f"Available balance is now: #{updated_bal}")
                                print("Thank you for banking with us 🤝")
                                with open(json_filepath, mode="w", encoding="utf-8") as file:
                                    json.dump(user_details, file, indent=4)
                                    break
                            else:
                                self.clear_screen()
                                print("Insufficient money to withdraw")
                                print(f"Available Balance: #{valid_acct[string_format][0][-3]}")
                        
                        except ValueError:
                            print("Type ammount in numbers only without any characters or symbols")


    # View user transaction history 
    def view_transaction_details(self, user_acct_num):
        user_details = self.load_json_file()
        transaction_history = ""
        for view in user_details:
            transaction_history = view[str(user_acct_num)][1]
        self.clear_screen()
        for x in transaction_history:
            print(f"{x}\t")

    # User's Transaction Limit
    def user_transaction_limit_operation(self, user_acct_num, transfer_attempt):
        user_details = self.load_json_file()
        current_date = datetime.datetime.now().date().strftime("%b %d, %Y")
        split_list = ""
        today_trans_list = []
        for all_transactions in user_details:
            if self.date_of_acct_created[0] == current_date:
                split_list = all_transactions[str(user_acct_num)][1]
        string = "Debit (Transfered)"
        for transaction in split_list:
            if current_date in transaction and string in transaction:
                # Use regular expression to find the amount after "Debit (Transfered):"
                match = re.search(r"Debit \(Transfered\): (\d+\.\d+|\d+)", transaction)
                if match:
                    # Convert the matched amount to float
                    amount = float(match.group(1))
                    today_trans_list.append(amount)
                else:
                    print("Amount not found.")
        total_tran_for_the_day = sum(today_trans_list)
        transfer_limit = 160000.0
        if total_tran_for_the_day + transfer_attempt == transfer_limit:
            return True
        elif total_tran_for_the_day + transfer_attempt < transfer_limit:
            return True
        elif total_tran_for_the_day + transfer_attempt > transfer_limit:
            print("You have reached your transfer limit for today, try again by 12:00am midnight.")
            return False

    # Json file for benefiary account numbers, account names, and bank names which will contain recipient's details
    def load_json_beneficiary_details(self):
        looping = True
        try:
            with open(json_beneficiary_filepath, mode="r", encoding="utf-8") as file:
                json_beneficiary = json.load(file)
                if json_beneficiary:
                    looping = False
                    return json_beneficiary
                    
        except (FileNotFoundError, json.JSONDecodeError):
            print("Beneficiary list is empty. Try to add the reciever's account number as beneficiary before you attempt to make transfers!")
            return False

        if not looping:
            return True
                            
    # Writes benefiary's details to JSON file
    def write_beneficiary_details_to_JSON(self, beneficiary_details):
        try:
            with open(json_beneficiary_filepath, mode="r", encoding="utf-8") as file:
                json_beficiaries = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            json_beficiaries = []
        json_beficiaries.append(beneficiary_details)
        with open(json_beneficiary_filepath, mode="w", encoding="utf-8") as file:
            json.dump(json_beficiaries, file, indent=4)

    # Ask user for benefiary account number
    def ask_valid_benefiary_acct_num(self):    
        looping = True
        benefiary_acct_num = input("Beneficiary account number: ")
        try:
            account_format = re.sub(r'[^0-9]', "", benefiary_acct_num)
            if account_format:
                if account_format.isdigit() and len(account_format) == 10:
                    looping = False
                    return account_format
                else:
                    raise KeyError
            else: 
                ValueError
        except ValueError:
            print("Only numbers are allowed!")
        except KeyError:
            print("Account number must be 10 digits")
        if not looping:
            return True
        return False
     
    # Ask for beneficiary account name
    def ask_valid_beneficiary_account_name(self):
        looping = True
        while looping:
            beneficiary_acct_name = input("Beneficiary account name: ").capitalize().strip()
            try:
                name_format = re.sub(r'^[a-zA-Z]+$', '', beneficiary_acct_name)
                if name_format:
                    looping = False
                    return name_format
                else:
                    raise ValueError
            except ValueError:
                print("Only numbers and letters are allowed")

    # Ask for beneficiary bank name
    def ask_valid_beneficiary_bank_name(self):
        looping = True
        while looping:
            beneficiary_bankname = input("Beneficiary bank name: ").capitalize().strip()
            try:
                bankname = re.sub(r'^[a-zA-Z]+$', '', beneficiary_bankname) 
                if bankname:
                    looping = False
                    return bankname
                else:
                    raise ValueError
            except ValueError:
                print("Enter bank name in this format e.g Gt bank, and only letters are allowed!")
   
   # Check if details in beneficiary list 
    def check_for_beneficiary(self, user_account_num):
        found = False
        beneficiary_list_exist = self.load_json_beneficiary_details()    
        account_num = self.ask_valid_benefiary_acct_num()
        for saved_acct in beneficiary_list_exist:
            if str(user_account_num) in saved_acct and account_num == saved_acct[str(user_account_num)][0]:
                print("Account Number: ", saved_acct[str(user_account_num)][0])
                print("Account Name: ", saved_acct[str(user_account_num)][1])
                print("Bank Name: ", saved_acct[str(user_account_num)][2])
                found = True
                return saved_acct[str(user_account_num)][1]
        if found:
            return True
        self.clear_screen()
        print("Account cannot be found in beneficiary list, Add account to beneficiary to enable tranfers")
        return False

    # User can search beneficiary account with name
    def check_beneficiary_with_name(self):
        found = False
        beneficiary_details = self.load_json_beneficiary_details()
        try:
            name = input("Search for beneficiary by name: ").strip()
            name_pattern = re.sub(r'[^a-zA-Z]+$', "", name)
            if name_pattern:
                for search in beneficiary_details: 
                    for account, details in search.items():
                        full_parts = details[1].split()
                        if any(name_pattern.lower() in part.lower() or name_pattern.capitalize() in part.capitalize() for part in full_parts):
                            print(details[1], details[0], details[2])
                            found = True
                if not found:
                    raise NameError      
            else:
                raise NameError
        except NameError:
            print("Name does not match any in beneficiary list, you can add details to beneficiary list!") 
        if found:
            return True
        return False

    # Prompt user to check for beneficiary either by name or account number
    def check_beneficiary_by_name_or_acct_num(self, user_account_num):
        looping = True
        while looping:
            search_option = input("Enter 'N' to search beneficiary by name or 'A' by account number:  ").lower()
            if search_option == "n":
                # This is just search for user input and print what matches
                if self.check_beneficiary_with_name():
                    print("Copy and paste the beneficiary account you want to transfer money into.")
                    # This will search for valid beneficiary account number and name, then return beneficiary name
                    name = self.check_for_beneficiary(user_account_num=user_account_num)
                    if name:
                        looping = False
                        return name
                break
            elif search_option == "a":
                # This will search for valid beneficiary account number and name, then return beneficiary name
                name = self.check_for_beneficiary(user_account_num=user_account_num)
                if name:
                    looping = False
                    return name
                else:
                    break
            else:
                self.clear_screen()
                print("Invalid input")
                looping = True
        if not looping:
            return True
             
    # Check if the benficiary account number already exist!
    def check_for_exist_beneficiary(self, user_account_num):
        beneficiary_details = self.load_json_beneficiary_details()
        acct_exist = False 
        exist_acct = self.ask_valid_benefiary_acct_num()
        for acct_num_exist in beneficiary_details:
            if exist_acct == acct_num_exist[str(user_account_num)][0]:
                acct_name = acct_num_exist[exist_acct][1]
                acct_exist = True     
        if acct_exist:
            self.clear_screen()
            print("Account number already exist with the account name: ",acct_name)
            return False
        return True
        
    # Save beneficiaries details to JSON file
    def accept_and_save_valid_beneficiary_details(self, user_account_num):
        exist = False
        check_beneficiary_list = self.load_json_beneficiary_details()
        beneficiary_details = {}
        beneficiary_acct_num = self.ask_valid_benefiary_acct_num()
        if check_beneficiary_list:
            for check_exist in check_beneficiary_list:
                if str(user_account_num) in check_exist:
                    if beneficiary_acct_num == check_exist[str(user_account_num)][0]:
                        exist_name = check_exist[str(user_account_num)][1]
                        exist = True
                        break
                else:
                    exist = False
            if exist:
                print("Account number already exist with the account name: ", exist_name)
                return False
            else:
                beneficiary_acct_name = self.ask_valid_beneficiary_account_name()
                beneficiary_bank_name = self.ask_valid_beneficiary_bank_name()
                beneficiary_phone_num = self.ask_valid_beneficiary_phonenum()
                beneficiary_details[str(user_account_num)] = [beneficiary_acct_num, beneficiary_acct_name, beneficiary_bank_name, beneficiary_phone_num]
                self.write_beneficiary_details_to_JSON(beneficiary_details=beneficiary_details)
                print(beneficiary_acct_name,"'s account details has been saved to your beneficiary list successfully!")
                return True
        
    
    # Ask the user for transfer amount and make sure they are figures
    def ask_transfer_amount(self, beneficiary_name):
        looping = True
        while looping:
            try:
                print("Enter figures of numbers only without use of comma(,) or dot(.)")
                transfer_amount = float(input(f"How much do you want to transfer to {beneficiary_name}? "))
                looping = False
                return transfer_amount
            except ValueError:
                print("Only numbers are allowed!")
                looping = True
        if not looping:
            return True
        return False
    
    # Proceed to make transfer with account number and pin
    def proceed_transfer(self, beneficiary_name, user_acct_no):    
        transfer_successful = False
        transfer_amount = self.ask_transfer_amount(beneficiary_name=beneficiary_name)
        if transfer_amount:
            update_user_bal = self.load_json_file()
            for sufficient_bal in update_user_bal:
                if str(user_acct_no) in sufficient_bal:
                    insufficient_bal = sufficient_bal[str(user_acct_no)][0][-3]
                    if transfer_amount < sufficient_bal[str(user_acct_no)][0][-3] and sufficient_bal[str(user_acct_no)][0][-3] > 5.0:
                        if self.user_transaction_limit_operation(user_acct_num=str(user_acct_no), transfer_attempt=transfer_amount):
                            avail_bal = sufficient_bal[str(user_acct_no)][0][-3] - transfer_amount
                            sufficient_bal[str(user_acct_no)][0][-3] = avail_bal
                            sufficient_bal[str(user_acct_no)][1].append(f"{self.date_of_acct_created[0]} {self.date_of_acct_created[1]}  {transfer_amount}      Debit (Transfered) to '{beneficiary_name}'")
                            transaction = sufficient_bal[str(user_acct_no)][1]
                            sufficient_bal[str(user_acct_no)][1] = transaction
                            self.clear_screen()
                            print(f"Transfer of {transfer_amount} to {beneficiary_name} was succesful ✅")
                            print(f"Available Balance: {avail_bal}")
                            with open(json_filepath, mode="w", encoding="utf-8") as file:
                                json.dump(update_user_bal, file, indent=4)
                                transfer_successful = True
                                break
                    else:
                        transfer_successful = False
                        self.clear_screen()
                        print("Insufficient balance")
                        print(f"Available Balance: {insufficient_bal}")
            if transfer_successful:
                return True
            return False

    # Transfer proceedure
    def transfer_procedure(self, valid_acct_no):
        saved_beneficiary = input("Is the account saved in beneficiary? (Y/N): ").lower()
        if saved_beneficiary == "yes" or saved_beneficiary == "y":
            beneficiary_details = self.load_json_beneficiary_details()
            if beneficiary_details:
                beneficiary_with_acct_num_or_name = self.check_beneficiary_by_name_or_acct_num(user_account_num=valid_acct_no)
                if beneficiary_with_acct_num_or_name:
                    go_ahead = input("Are you sure of the details to make sure transfer? (Y/N): ").lower()
                    if go_ahead == "yes" or go_ahead == "y":
                        self.proceed_transfer(beneficiary_name=beneficiary_with_acct_num_or_name, user_acct_no=valid_acct_no)
                        return True
                    else:
                        self.clear_screen()
                else:
                    self.accept_and_save_valid_beneficiary_details(user_account_num=valid_acct_no)
            else:
                self.accept_and_save_valid_beneficiary_details(user_account_num=valid_acct_no)
        elif saved_beneficiary == "no" or saved_beneficiary == "n":
            self.accept_and_save_valid_beneficiary_details(user_account_num=valid_acct_no)

    # Ask for beneficiary phone number
    def ask_valid_beneficiary_phonenum(self):
        looping = True
        while looping:
            beneficiary_phonenum = input("Beneficiary phonenumber: ")
            try:
                phonenumber = re.sub(r'[^0-9]', '', beneficiary_phonenum)
                if phonenumber:
                    looping = False
                    return phonenumber
                else:
                    raise ValueError
            except ValueError:
                print("Only numbers are allowed!")


    # User should be able to export their transaction history to external file like csv
    def export_transaction_history_to_csv(self, user_account_num):
        user_details = self.load_json_file()
        string_acct_num = str(user_account_num)
        user_valid_name = ""
        trans_history = ""
        found_history = False
        if user_details:
            for valid_user in user_details:
                if string_acct_num in valid_user and valid_user[string_acct_num][1] != []:
                    user_valid_name = f"{valid_user[string_acct_num][0][1]} {valid_user[string_acct_num][0][0]}"
                    trans_history = valid_user[string_acct_num][1]
                    found_history = True

            if found_history:
                # Open the file in write mode ('w') only once, outside the loop
                with open(f"{csv_file_path}/{user_valid_name}.csv", mode="w", encoding="utf-8", newline="") as file:
                    writer = csv.writer(file)
                    
                    # Loop through each transaction in the transaction history and write it to the file
                    for each_transaction in trans_history:
                        writer.writerow([each_transaction])
                self.clear_screen()
                print(f"Your transaction history has been exported to {csv_file_path}/{user_valid_name}.csv file successfully!")
                return True

            # Print message to user if transaction history is empty
            else:
                print("Transaction history is empty, nothing to export!")
                return False

    # Asks for user operations
    def user_operation():
        choice = input("Type 'C' for create an account, 'D' for deposit, 'W' for withdraw, 'B' to check balance, 'X' to check biography, 'T' for transfer, 'V' to view transaction history, 'E' to export transaction history, 'exit' to exit: ")
        return choice
            
    # Os function to clear screen 
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        
