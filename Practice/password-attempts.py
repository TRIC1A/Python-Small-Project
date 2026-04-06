# Password Attempts
# Ask a user to enter password
# Allow only 3 attempts
# Show success or failure

# 1. Enter a user password
# 2. check if the password is equal to the user input password
# 3. count the attempts
# 4. if the attempts is equal to 3
# 5. print either success or failed


# 1. ask the user input 
# 2. check if the password is incorrect
# 3. if incorrect count it as 1 attempt
# 4. if its correct, check how many attempt did the user guess the correct password
# 5. if whithin 3 attempts print "You successfully guess the password"
# 6. if its greater that 3 print "Try again." or "You failed to guess the password" 


# password
password = "admin123"
total_attempts = 3
count = 0
while True:
    user_attempt = input("Enter a correct password: ")
    count += 1
    
    if user_attempt == password:
        print("You successfully guess the password")
        break
    else:
        if count >= total_attempts:
            print("You failed to guess the password.")
            print(f"Your total attempts is: {count}")
            

    
    
    
        
        
    
    
