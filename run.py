from bank_atm_simulation import Create_User_Account


print("Hello, Welcome to Finance your money ATM! 🤝")
operating = True
# Creates empty string for user at first, after user's details has been valid, theb we'll replace with user's details
user = Create_User_Account(fname="", lname="", middlename="", gender="", date_of_birth="", next_of_kin="", email="", residential_address="", phonenumber="", state_of_origin="", nationality="", next_of_kin_rel="")
while operating: 
    choice = input("Type 'C' for create an account, 'D' for deposit, 'W' for withdraw, 'B' to check balance, 'X' to check biography, 'exit' to exit: ") 
    match choice:
        case "C" | "c":
            print("Note: Numbers and symbols are not allowed except you're instructed to add, else it'll be removed and replace with just alphabets(a-z or A-Z)")
            
            firstname = user.get_valid_firstname()
            lastname = user.get_valid_last_name()
            middlename = user.get_valid_middlename()
            gender = user.get_valid_gender()
            birth_date = user.get_valid_date_of_birth()
            nationality = user.get_valid_nationality()
            state_of_origin = user.get_valid_state_of_origin()
            residential_add = user.get_valid_residential_address()
            email = user.get_valid_email()
            call_number = user.get_valid_phone_number()
            next_of_kin = user.get_valid_next_of_kin()
            next_of_kin_rel = user.get_valid_next_of_kin_rel()
            # Make sure user have the expected pin format before showing the account number generated.
            pin = user.create_user_pin()
            acct_num = user.generate_account_number()
            # Create user object with the required inputs
            user = Create_User_Account(fname=firstname, lname=lastname, middlename=middlename, gender=gender, date_of_birth=birth_date, next_of_kin=next_of_kin, email=email, residential_address=residential_add, phonenumber=call_number, state_of_origin=state_of_origin, nationality=nationality, next_of_kin_rel=next_of_kin_rel)

            # User gets free 5 naira for the first time of opening an account
            account_balance = float(f"{user.user_balance + 5.00}")
            # Fill in the user's required input to be saved in json
            user.user_details[acct_num] = [user.firstname, user.lastname, user.middlename, user.gender, user.date_of_birth, user.email, user.phonenumber, user.residential_address, user.state_of_origin, user.nationality, user.next_of_kin, user.next_of_kin_rel, account_balance, pin, user.date_of_acct_created], []

            # Load json and write user details to file
            user_details = user.add_user_details_to_json(user_details=user.user_details)
            user.clear_screen()
            print(f"Account created successfully!\nHere is your account number {acct_num}\nAccount balance: #{account_balance}\nMake sure you save your details for future transactions.")
                        
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
        
        case "T" | "t":
            valid_user = user.validate_user_details()
            if valid_user:
                user.transfer_procedure(valid_acct_no=valid_user)
                
        case "X" | "x":
            valid_user = user.validate_user_details()
            if valid_user:
                user.biography(account_num=valid_user)

        case "V" | "v":
            valid_user = user.validate_user_details()
            if valid_user:
                user.view_transaction_details(user_acct_num=valid_user)

        case "E" | "e":
            valid_user = user.validate_user_details()
            if valid_user:
                user.export_transaction_history_to_csv(user_account_num=valid_user)

        case "Exit" | "exit":
            print("Bye!")
            break

        case _:
            print("Invalid input")
            user.clear_screen()
