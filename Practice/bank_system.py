# Bank System
# 1. Deposit
# 2. Withdraw
# 3. Show balance

# flow
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
# 2. Add a multi user accounts
# 3. add transfer money ✔
# 4. add pin number in (login, witdrawal, transfer money, delete account)
# 5. add delete account
# 6. update account info
#   > change name or PIN
# 7. Save to File
#   > Store data even after program closes
# 8. Add a database into the system
# 9. in the transaction add the DATE when the transaction begin


# Use functions for better calling


# import mysql.connector
import random
from datetime import datetime


accounts = {
    1111: {"name": "tricia", "pin": "1234", "balance": 0, "transactions": []},
    1122: {"name": "gale", "pin": "5678", "balance": 0, "transactions": []},
    2222: {"name": "kit", "pin": "4321", "balance": 0, "transactions": []},
    2233: {"name": "kae", "pin": "8765", "balance": 0, "transactions": []}
}


def main_menu():
    """MAIN MENU"""
    while True:
        print("\n[1] Login")
        print("[2] Exit")
        try:
            choice = int(input("Choose: "))
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
    account_name = input("\nAccount Name: ")
    account_number = int(input("Account Number: "))
    if account_number in accounts and accounts[account_number]["name"] == account_name:
        if authenticate(account_number):
            print("Login successful")
            bank_menu(account_number)   # pass only the account number
        else:
            print("Wrong PIN. Access denied.")
    else:
        print("Wrong account name or account number")
            

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
                    
                    # added timestamps when the transfer happened
                    transaction_id = random.randint(100000, 999999)
                    timestamp = get_current_time()
                    
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
    main_menu()
                
