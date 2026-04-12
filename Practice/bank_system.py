# Bank System (No name yet for the system)
# 1. Deposit
# 2. Withdraw
# 3. Transfer Money
# 4. View Balance
# 5. Transaction History

# flow in the bank_menu
# 1. ask the user a choice
# 2. in deposit 
#   > ask user how much money need to deposit(limit: 100000)
# 3. in withdraw 
#   > ask user how much money to withdraw
#   > check if the withdraw is less than whats in the balance
# 4. in show balance
#   > show how much balance the user currently have
#   > create a variables to store the balance money of the user


# Note!!!
# need to add the [] to store a value and save all the transaction history



# transfer money
# 1. enter the recipient account ID
# 2. Authenticate sender(PIN, password)
# 3. Enter transfer amount 
# > sender must have enough balance
# > amount is valid (within limits)
# 4. confirm transaction details (show sender, recipient,amount, and update balance before finalizing)
# 5. Execute transfer (update both accounts automatically, either both balances update or none to avoid inconsistencies)
# 6. print success/failure message with transaction ID for tracking



# INCOMING UPDATES OF THE SYSTEM!!!!
# 1. add account name and account number ✔
# 2. Add a multi user accounts ✔
# 3. add transfer money ✔
# 4. add pin number in (login, witdrawal, transfer money, delete account) ✔
# 5. create, search, view, update and delete account(admin only)
# 6. update account info
#   > change name or PIN
# 7. Save to File   ✔
#   > Store data even after program closes
# 8. Add a database into the system
# 9. in the transaction add the DATE when the transaction begin ✔
# 10. user and admin can update or edit the pin and name 
#   > user should have a certain restriction in terms of changing or updating user information should verify first the (PIN, name)
#   > admin can change user PIN without verifying the old PIN


# FUTURE IMPROVEMENTS
# 1. ADMIN SYSTEM UPGRADES
#   > Admin security upgrade (limit the wrong password attempts[3 tries lock])
# 2. USER ACCOUNT UPGRADES
#   > change name 
#   > change PIN(with old PIN verification)
# 2. ACCOUNT SECURITY
#   > Lock account after 3 wrong PIN attempts
#   > Unlock via admin only





# Use functions for better calling


# import mysql.connector
import random
from datetime import datetime
import json



accounts = {
    1111: {"name": "tricia", "pin": "1234", "balance": 0, "transactions": [], "status": "active", "locked": False},
    1122: {"name": "gale", "pin": "5678", "balance": 0, "transactions": [], "status": "active", "locked": False},
    2222: {"name": "kit", "pin": "4321", "balance": 0, "transactions": [], "status": "active", "locked": False},
    2233: {"name": "kae", "pin": "8765", "balance": 0, "transactions": [], "status": "active", "locked": False}
}

admin_password = "admin123"

def save_data():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)
        

def load_data():
    global accounts
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)  
            
            accounts = {int(k): v for k, v in accounts.items()}
    except FileNotFoundError:
        print("No saved data found. Using default accounts.")

# Main Menu
def main_menu():
    """MAIN MENU"""
    while True:
        print("\n[1] Login")
        print("[2] Exit")
        
        choice = input("Choose: ")      # make it string first to pass in the admin login
        
        if choice.lower() == "admin":
            admin_login()
            continue
        try:
            choice = int(choice)    # updated it to integer to continue to access the user login/exit
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        match(choice):
            case 1:
                user_login()
            case 2:
                print("Exiting the system...")
                print("Thank you for using our system!!!")                
                break
                   
              
# user login   
def user_login():
    """ LOGIN """
    attempt = 0
    valid_account = None        # track only correct account
    
    while attempt < 3:
        account_name = input("\nAccount Name: ")
        
        try:
            account_number = int(input("Account Number: "))
        except ValueError:
            print("Invalid account number.")
            attempt += 1
            continue
        
        if account_number in accounts and accounts[account_number]["name"].lower() == account_name:
            
            # check if account is locked
            if accounts[account_number].get("locked"):
                print("Account is locked. Contact admin.")
                return
                
            valid_account = account_number
            
            if authenticate(account_number):
                print("Login successfull.")
                bank_menu(account_number)
                return
            else:
                print(f"Wrong PIN. Attempts left: {2 - attempt}")
                attempt += 1
        else:
            print("Wrong account name or account number.")
            attempt += 1
    
    if valid_account is not None:
        accounts[valid_account]["locked"] = True
        save_data()
        print("Too many failed attempts. Account is now locked.")
    
    print("Returning to main menu.")
    

            
    
def admin_login():
    
    # admin_password = "admin123"
    password = input("Enter admin password: ")
    if password == admin_password:
        print("You can acceses now the admin menu.")
        admin_menu()
    else:
        print("Access denied.")
        return
        

# SECRET ACCESS FOR ADMIN
def admin_menu():
    
    print("\n========== Admin Menu ==========")
        
    while True:
        print("\n[1] Create Account")
        print("[2] Read/View Accounts")
        print("[3] Update Account")
        print("[4] Search Account")
        print("[5] Delete Account")
        print("[6] View Admin Logs")
        print("[7] Back")
        try:    
                choice = int(input("Choose: "))     
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        match(choice):
            case 1:     # Create Account
                account_name = input("Enter Account Name: ")
                account_number = int(input("Enter Account Number: "))
                pin = input("Enter PIN: ")  
                
                # check if the account already exists
                if account_number in accounts:
                    print("Acount Number already exists.")
                else:
                    accounts[account_number] = {
                        "name": account_name,
                        "pin": pin,
                        "balance": 0,
                        "transactions": []
                    }
                    save_data()
                    print("Account successfully created.")
            
            case 3:     # Update Account
                update_account = int(input("Enter Account Number to update: "))     # new account number 
                if update_account in accounts:
                    print("[1] Change Name")
                    print("[2] Change PIN")
                    # print("[3] Change Account Status")  
                    try:    
                            choice = int(input("Choose: "))     
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
                    
                    if choice == 1:
                            new_account_name = input("Enter New Account Name: ")
                            
                            if not new_account_name.strip():
                                print("Name cannot be empty.")
                                continue
                            
                            accounts[update_account]['name'] = new_account_name
                            save_data()
                            print(f"Account {update_account} name updated successfully.")
                            
                    elif choice == 2:
                        new_pin = input("Enter new PIN: ")
                        
                        if not new_pin.isdigit() or len(new_pin) != 4:
                            print("PIN must be exactly 4 digits.")
                            continue
                        
                        confirm = input("Are you sure? [Y/N]: ")
                        
                        if confirm != 'Y':
                            print("PIN cancelled.")
                            continue
                        
                        accounts[update_account]["pin"] = new_pin
                        save_data()
    
                else:
                    print("Account not found.")
                    
            
            case 5:     # Delete Account
                remove_account = int(input("Enter Account Number to delete: "))
                if remove_account in accounts:
                    del accounts[remove_account]
                    save_data()
                    print(f"\nAccount {remove_account} deleted successfully.")
                else:
                    print("Incorrect account number.")
                    
                    exit = input("Do you want to try again? [Y/N]: ").upper()
                    
                    if exit == 'N':
                        return
                    else:
                        continue                
                
            case 7:
                return
                
                
#  get the current time
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def authenticate(account_id):
    entered_id = input("Enter PIN: ")
    return accounts[account_id]["pin"] == entered_id
    

# bank menu of the user
def bank_menu(sender_id):
    acc = accounts[sender_id]   # get the account dictionary
    
    while True:
        print(f"\n========== Welcome User: {acc['name']} ==========")
        print("[1] Deposit")   
        print("[2] Withdraw")
        print("[3] Transfer Money")
        print("[4] View Balance")
        print("[5] Transaction History")
        print("[6] Logout")
        try:
            choice = int(input("Choose [1-6]: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        match(choice):
            case 1:     # Deposit
                try:
                    amount = int(input("\nEnter amount: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                
                if amount <= 0:
                    print("Invalid amount.")
                elif amount > 100000:
                    print("You exceed the limit to deposit: ")
                else:
                    acc['balance'] += amount
                    save_data()
                    
                    # added timestamps when the transfer happened
                    transaction_id = random.randint(100000, 999999)
                    timestamp = get_current_time()
                    
                    acc["transactions"].append({
                        "id": transaction_id,
                        "type": "deposit", 
                        "amount": amount,
                        "time": timestamp
                    })
                    print(f"\nDeposited: {amount}\nNew Balance: {acc['balance']:.2f}")
                    
            case 2:     # Withdraw
                
                if not authenticate(sender_id):
                    print("Authentication failed. Wrong PIN.")
                    continue
                
                try:
                    withdraw = int(input("\nEnter amount: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                
                if withdraw > acc['balance']:
                    print("Insuficient money.")
                    print(f"Your current balance: {acc['balance']:.2f}")
                # i dont think this line of code will appear in the terminal 
                elif acc['balance'] - withdraw < 500:
                    print(f"You must maintain at least 500 balance.")
                else:
                    acc['balance'] -= withdraw
                    save_data()
                    
                    # added timestamps when the transfer happened
                    transaction_id = random.randint(100000, 999999)
                    timestamp = get_current_time()          # added timestamps when the transfer happened
                    
                    acc["transactions"].append({
                        "id": transaction_id,
                        "type": "withdraw", 
                        "amount": withdraw,
                        "time": timestamp
                    })
                    print(f"\nWithdraw: {withdraw}\nNew Balance: {acc['balance']:.2f}")
            
            case 3:     # Transfer Money
                """ Transfer Money """
                if not authenticate(sender_id):
                    print("Authentication failed. Wrong PIN.")
                    continue
                
                try:
                    recipient_id = int(input("Enter Recipient Account Number: "))  
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                 
                
                if recipient_id == sender_id:
                    print("You cannot transfer to your own account.")
                    continue
                            
                if recipient_id in accounts:
                    transfer_amount = int(input("Enter amount: "))
                    
                    if transfer_amount > acc['balance']:
                        print("Insuficient funds.")
                    elif acc['balance'] - transfer_amount < 500:
                        print("Cannot transfer, maintaining balance requirement not met.")
                    else:
                        choice = input("Confirm transfer? [Y/N]: ").upper()
                        
                        if choice == "Y":
                            
                            
                            transaction_id = random.randint(100000, 999999)
                            timestamp = get_current_time()      # added timestamps when the transfer happened
                            
                            acc['balance'] -= transfer_amount
                            accounts[recipient_id]['balance'] += transfer_amount
                            save_data()
                            
                            acc["transactions"].append({
                                "id": transaction_id,
                                "type": "transfer_out", 
                                "amount": transfer_amount, 
                                "to": recipient_id,
                                "time": timestamp
                            })
                            accounts[recipient_id]["transactions"].append({
                                "id": transaction_id,
                                "type": "transfer_in", 
                                "amount": transfer_amount, 
                                "from": sender_id,
                                "time": timestamp
                            })
                            print(f"Transfer successful!\nNew Balance: {acc['balance']:.2f}")
                        else:
                            print("Transfer cancelled.")
                else:
                    print("Recipient account not found.") 
                            
            case 4:     # Show Balance
                print(f"\nYour balance is: {acc['balance']:.2f}")
                
            case 5:     # Transaction History
                print("\n========== TRANSACTION HISTORY ==========")
                
                if not acc["transactions"]:
                    print(("No transaction yet."))
                else:
                    print("-" * 95)
                    print(f"{'ID':<10}{'TYPE':<20}{'DETAILS':<30}{'AMOUNT':<15}{'DATE'}")
                    print("-" * 95)
                    
                    for tran in acc["transactions"]:
                        t_id = tran["id"]
                        t_type = tran["type"]
                        amount = tran["amount"]
                        time = tran["time"]
                        
                        if t_type == "deposit":
                            details = "Cash Deposit"
                            sign = "+"
                        
                        elif t_type == "withdraw":
                            details = "ATM Withdrawal"
                            sign = "-"
                        
                        elif t_type == "transfer_out":
                            recipient = tran["to"]
                            details = f"To {recipient} ({accounts[recipient]['name']})"
                            sign = "-"
                            
                        elif t_type == "transfer_in":
                            sender = tran["from"]
                            details = f"From {sender} ({accounts[sender]['name']})"
                            sign = "+"
                        
                        print(f"{t_id:<10}{t_type.upper():<20}{details:<30}{sign}{amount:<15.2f}{time}")
                                   
            case 6:     # Logout
                print("Logging out...")
                print("Thank you for using our service!!!")
                break
            
            

if __name__ == "__main__":
    load_data()
    main_menu()
                
