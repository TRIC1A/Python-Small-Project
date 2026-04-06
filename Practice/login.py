# Login
# 1. ask username and password
# 2. check if correct

# Rule:
# 1. username: admin
# 2. password: 1234

# flow
# 1. store the value of the username and password in a variables
# 2. ask a user a username ans password
# 3. use a loop and check if the username/password is correct
# 4. print if the login is failed or success

# suggestion
# use "try" for error handling
# example:
# try:
#     passwords = int(input("Enter password: "))
# except ValueError:    #Invalid conversion
#     print("Invalid input!Please enter number only.")
#     continue



username = "admin"
password = "1234"

while True:
    print("\n========== LOGIN SYSTEM ==========")
    user = input("Enter username: ")
    passwords = input("Enter password: ")

    if (user == username) and (password == passwords):
        print("Login successful")
        break
    else:
        print("Login failed")
    
    exit = input("Do you want to try again [Y/N]: ").upper()
    
    if exit == 'N':
        print("Exiting...")
        break