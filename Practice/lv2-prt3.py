# Sum of Numbers
# ask user for number continuously until the user enter the 0 then compute the user input before the 0

# 1. use while loop 
# 2. ask the user a number
# 3. check if the user enter a 0
# 4. if no continue the loop
# 5. if yes then start computing all the number the use inputed
# 6. Sum it all and print

while True:
    number = int(input("Enter a number:"))
    if number == 0:
        sum += number
        print(f"The sum of all the input number is: {sum}")
        
    