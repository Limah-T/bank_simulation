ATM System Simulation
Overview
This is an ATM system simulation project that allows users to create accounts, deposit and withdraw funds, check balances, transfer money, and view transaction history.

Features
Create Account
Deposit Funds
Withdraw Funds
Check Balance
Transfer Funds
Transaction History
Export Transactions to CSV
Technology Stack
Python
Cryptography
JSON for data storage
Data Storage with JSON
For data persistence, this system uses JSON files to store user account details and transaction history. JSON is used because it is human-readable, easy to modify, and portable across platforms.

Instructions for Use
Running the Program
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python run.py
Basic Commands
Create Account: 'C'
Deposit: 'D'
Withdraw: 'W'
Check Balance: 'B'
Transfer Funds: 'T'
View Transaction History: 'V'
Export Transaction History: 'E'
Exit: 'exit'
Example of JSON Structure
json
Copy code
{
    "5486109723": [
        ["Halimah", "Temitope", "Kolapo", "Female", "07 Aug, 1990", "kolapo@gmail.com", "09130030948", "Surulere, LAGOS", "Kwara state", "Nigerian", "Rokeeb", "Brother", 425018.0, "Encrypted_PIN", ["Jan 07, 2025", "12:42pm"]],
        ["Jan 07, 2025 02:20pm 250000.0 Credit (Deposited)", "Jan 07, 2025 02:29pm 30000.0 Debit (Withdrew)", "Jan 07, 2025 02:50pm 26000.0 Debit (Transfered) to 'Kolapo taiwo'"]
    ]
}