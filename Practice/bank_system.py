# Bank System
# 1. Deposit
# 2. Withdraw
# 3. Show balance

# flow
# 1. ask the user a choice [1-4]
# 2. in deposit 
#   > ask user how much money need to deposit(limit: 100000)
# 3. in withdraw 
#   > ask user how much money he will withdraw
#   > check is the withdraw is less that whats in the balance
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


accounts = {
    1111: {"name": "tricia", "balance": 0, "transactions": []},
    1122: {"name": "gale", "balance": 0, "transactions": []},
    2222: {"name": "kit", "balance": 0, "transactions": []},
    2233: {"name": "kae", "balance": 0, "transactions": []}
}


def main_menu():
    """MAIN MENU"""
    while True:
        print("\n[1] Login")
        print("[2] Exit")
        choice = int(input("Choose: "))
        
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
        print("Login successful")
        bank_menu(account_number)   # pass only the account number
    else:
        print("Wrong account name or account number")
            
    
# bank menu of the user
def bank_menu(sender_id):
    acc = accounts[sender_id]   # get the account dictionary
    
    while True:
        print(f"\n========== Welcome         User: {acc["name"]} ==========")
        print("[1] Deposit")   
        print("[2] Withdraw")
        print("[3] Transfer Money")
        print("[4] View Balance")
        print("[5] Transaction History")
        print("[6] Logout")
        choice = int(input("Choose [1-6]: "))
        
        match(choice):
            case 1:     # Deposit
                amount = int(input("\nEnter amount: "))
                if amount >= 100000:
                    print("You exceed the limit to deposit: ")
                else:
                    acc["balance"] += amount
                    acc["transactions"].append({"type": "deposit", "amount": amount})
                    print(f"\nDeposited: {amount}\nNew Balance: {acc["balance"]:.2f}")
                    
            case 2:     # Withdraw
                withdraw = int(input("\nEnter amount: "))
                if withdraw > acc["balance"]:
                    print("Insuficient money.")
                    print(f"Your current balance: {acc["balance"]:.2f}")
                # i dont think this line of code will appear in the terminal 
                elif acc["balance"] < 500:
                    print(f"You cannot withdraw.\nYour balance is currently: {acc["balance"]:.2f}.\nYou need to withdraw atleast greater than 500 pesos.")
                else:
                    acc["balance"] -= withdraw
                    acc["transactions"].append({"type": "withdraw", "amount": withdraw})
                    print(f"\nWithdraw: {withdraw}\nNew Balance: {acc["balance"]:.2f}")
            
            case 3:     # Transfer Money
                """ Transfer Money """
                recipient_id = int(input("Enter Recipient Account Number: "))   
                            
                if recipient_id in accounts:
                    transfer_amount = int(input("Enter amount: "))
                    
                    if transfer_amount > acc["balance"]:
                        print("Insuficient funds.")
                    elif acc["balance"] - transfer_amount < 500:
                        print("Cannot transfer, maintaining balance requirement not met.")
                    else:
                        choice = input("Confirm transfer? [Y/N]: ").upper()
                        if choice == "Y":
                            acc["balance"] -= transfer_amount
                            accounts[recipient_id]["balance"] += transfer_amount
                            
                            acc["transactions"].append({
                                "type": "transfer_out", 
                                "amount": transfer_amount, 
                                "to": recipient_id
                            })
                            accounts[recipient_id]["transactions"].append({
                                "type": "transfer_in", 
                                "amount": transfer_amount, 
                                "from": sender_id
                            })
                            print(f"Transfer successful!\nNew Balance: {acc["balance"]:.2f}")
                        else:
                            print("Transfer cancelled.")
                else:
                    print("Recipient account not found.") 
                            
            case 4:     # Show Balance
                print(f"\nYour balance is: {acc["balance"]:.2f}")
                
            case 5:     # Transaction History
                print(f"\n--- Transaction History ---")
                for tran in acc["transactions"]:
                    if tran["type"] == "deposit":
                        print(f"    + Deposit         : {tran['amount']:.2f}")
                    elif tran["type"] == "withdraw":
                        print(f"    - Withdraw        : {tran['amount']:.2f}")
                    elif tran["type"] == "transfer_out":       
                        recipient_id = tran["to"]   # get the recipient account number from transaction
                        print(f"    -> Transfer Out   : {tran['amount']:.2f} to {recipient_id} ({accounts[recipient_id]["name"]})")
                    elif tran["type"] == "transfer_in":
                        sender_id = tran["from"]    # get sender account number from transaction
                        print(f"    <- Transfer In   : {tran['amount']:.2f} from {sender_id} ({accounts[sender_id]["name"]})")
                    else:
                        print("There are no transaction yet.")
                    
            case 6:     # Logout
                print("Logging out...")
                print("Thank you for using our service!!!")
                break
            
            
            
            


if __name__ == "__main__":
    main_menu()
                
