from datetime import datetime

# # greeting
# name = input("Enter your name: ")
# print("Hello", name, ".You passed the level 1 exercise problem!!!")


# Age Calculator
current_date = datetime.now()

print(f"Today's Date: {current_date.strftime('%B, %d, %Y')}")
print(f"Current Year: {current_date.year}")

# Get birth date of the user
birth_date = datetime.strptime(input("Enter your birthdate (YYYY-MM-DD): "), "%Y-%m-%d")

# Calculate the age correctly
age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

print(f"You are {age} years old")
print(f"You're birthday is on {birth_date.strftime('%B %d, %Y')}")
