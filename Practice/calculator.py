# calculator
# 1. ask first for the number
# 2. ask for the operator(+,-,*,/)
# 3. ask again a number
# 4. then calculate the total

num1 = int(input("Enter a first number: "))
operator = input("Enter a operator (+,-,*,/): ")
num2 = int(input("Enter a second number: "))

match operator:
    case '+':
        addition = num1 + num2
        print(f"{num1} {operator} {num2} = {addition}")
    case '-':
        subtraction = num1 - num2
        print(f"{num1} {operator} {num2} = {subtraction}")
    case '*':
        product = num1 * num2
        print(f"{num1} {operator} {num2} = {product}")
    case '/':
        division = num1 / num2
        print(f"{num1} {operator} {num2} = {division}")