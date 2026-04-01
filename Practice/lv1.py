# # greeting
# name = input("Enter your name: ")
# print("Hello", name, ".You passed the level 1 exercise problem!!!")


from datetime import datetime

# Age Calculator

current_date = datetime.now()

print(f"Today's Date: {current_date.strftime("%B, %d, %Y")}")
print(f"Current Year: {current_date.year}")

birth_date = datetime.strptime(input("Enter your birthday [YYYY-MM-DD]: "), "%Y-%m-%d")

age = current_date.year - birth_date.year -((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

print(f"You are {age} years old")
