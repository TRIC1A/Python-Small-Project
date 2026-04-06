# Multiplication table
# need to ask the user the number and display its multiplication table
# 1. ask user the number 
# 2. create a for loop where it will display all the multiplication table

# use the range(start,stop)
# usage: the stop value is always excluded, so need to add 1 to get the number you want
# default start is 0
# default step is 1
# Negative step goes backwards


# enter a number and display all multipication table
# example: enter a number: 3
# display: 3 * 1 = 3  - 3 * 10 = 20


number = int(input("Enter a number: "))

for num in range(1, 11):
    answer = number * num
    print(f"{number} * {num} = {answer}")