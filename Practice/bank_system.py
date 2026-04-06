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


# INCOMING UPDATES OF THE SYSTEM!!!!
# 1. add account name and account number ✔
# 2. Add a multi user accounts
# 3. add transfer money
# 4. add pin number in (login, witdrawal, transfer money, delete account)
# 5. add delete account
# 6. update account info
#   > change name or PIN
# 7. Save to File
#   > Store data even after program closes


# Use functions for better calling


# import mysql.connector


accounts = [
    {"name": "tricia", "number": 1111, "balance": 0, "transactions": []},
    {"name": "gale", "number": 1122, "balance": 0, "transactions": []}
]


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
    print("\nLOGIN")
    account_name = input("Account Name: ")
    account_number = int(input("Account Number: "))
    for acc in accounts:
        if acc["name"] == account_name and acc["number"] == account_number:
            print("Login successful")
            bank_menu(acc)
            return
    print("Wrong account name or account number")
            
    
# bank menu of the user
def bank_menu(acc):
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
                elif acc["balance"] < 500:
                    print(f"You cannot withdraw.\nYour balance is currently: {acc["balance"]:.2f}.\nYou need to withdraw atleast greater than 500 pesos.")
                else:
                    acc["balance"] -= withdraw
                    acc["transactions"].append({"type": "withdraw", "amount": withdraw})
                    print(f"\nWithdraw: {withdraw}\nNew Balance: {acc["balance"]:.2f}")
            
            case 3:     # Transfer Money
                print("\nComing Soon...")
        
            case 4:     # Show Balance
                print(f"\nYour balance is: {acc["balance"]:.2f}")
                
            case 5:     # Transaction History
                print(f"\nTransaction History for {acc["name"]}")
                for tran in acc["transactions"]:
                    if tran["type"] == "deposit":
                        print(f"    + Deposit   : {tran['amount']:.2f}")
                    elif tran["type"] == "withdraw":
                        print(f"    - Withdraw  : {tran['amount']:.2f}")
                    else:
                        print("There are no transaction yet.")
                    
            case 6:     # Logout
                print("Thank you for using our service!!!")
                break
            
            
            
            


if __name__ == "__main__":
    main_menu()
                
