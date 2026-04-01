while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
    
    exit = input("Do you want to try and enter a number again? [Y/N]: ").upper()
    
    if exit == 'N':
        print("Exiting...")
        break