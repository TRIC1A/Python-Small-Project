import random

# Number Guessing Game
# need to use the random methods between 1 - 10
# 1. create a variable number 1 - 10
# 2. create a variable called computer_choice between the varibales that you created
# 3. ask the user the number
# 4. create a loop where it will check if the user and the computer is match or not

# Adding features add a 3 lifeline

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Available options: {options}")
computer_choice = random.choice(options)
user_choice = int(input("Enter a number between [1-10]: "))

while True:
    if(user_choice == computer_choice):
        print(f"It's a match!!\nyou pick: {user_choice}\ncomputer pick: {computer_choice}")
        break
    elif(user_choice > computer_choice):
        print("Enter a lower number")
    elif(user_choice < computer_choice):
        print("Enter a higher number")
    else:
        print("Try again!!!")
        
        exit = input("Do you wan to try and guess a number again [Y/N]: ").upper()
        if exit == 'N':
            print("Exiting the program...")
            break
        
    user_choice = int(input("Enter a number between [1-10]: "))