# Bank System
# 1. Deposit
# 2. Withdraw
# 3. Show balance

# flow
# 1. ask the user a choice [1-4]
# 2. in deposit 
#   > ask user how much money need to deposit(limit: 50000)
# 3. in withdraw 
#   > ask user how much money he will withdraw
#   > check is the withdraw is less that whats in the balance
# 4. in show balance
#   > show how much balance the user currently have
#   > create a variables to store the balance money of the user


# Note!!!
# need to add the [] to store a value and save all the transaction history


# INCOMING UPDATES OF THE SYSTEM!!!!
# 1. add account name and account number
# 2. Add a multi user accounts
# 3. add transfer money
# 4. add pin number in (login, witdrawal, transfer money, delete account)
# 5. add delete account
# 6. update account info
#   > change name or PIN
# 7. Save to File
#   > Store data even after program closes


# Use functions for better calling

balance = 0
transactions = []
while True:
    print("\n========== BANK SYSTEM ==========")
    print("[1] Deposit")
    print("[2] Withdraw")
    print("[3] View Balance")
    print("[4] Exit")
    choice = int(input("Choose [1-4]: "))
    
    match(choice):
        case 1:     # Deposit
            amount = int(input("\nEnter amount: "))
            if amount >= 100000:
                print("You exceed the limit to deposit: ")
            else:
                balance += amount
                transactions.append({"type": "deposit", "amount": amount})
                print(f"\nDeposited: {amount}\nNew Balance: {balance}")
                
        case 2:     # Withdraw
            withdraw = int(input("\nEnter amount: "))
            if withdraw > balance:
                print("Insuficient money.")
                print(f"Your current balance: {balance}")
            elif balance < 500:
                print(f"You cannot withdraw.\nYour balance is currently: {balance}.\nYou need to withdraw atleast greater than 500 pesos.")
            else:
                balance -= withdraw
                transactions.append({"type": "withdraw", "amount": withdraw})
                print(f"\nWithdraw: {withdraw}\nNew Balance: {balance}")
    
        case 3:     # Show Balance
            print(f"\nYour balance is: {balance}")
            print("\nTransaction History")
            for tran in transactions:
                print(f"    {tran['type']}: {tran['amount']}")
        case 4:
            print("Thank you for using our service!!!")
            break
            
                
