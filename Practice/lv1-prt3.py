# find the largest number
# 1. enter the first number
# 2. enter the second number
# 3. enter the third number
# 4. check the number of the first 2 number to know the large number
# 5. after checking the first 2 number and knowiing the large number 
# 6. check the third number and compare if its larger or not
#  7. print the largest number

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    largest = max(num1,num2,num3)
        
    print(f"Largest: {largest}")
    




