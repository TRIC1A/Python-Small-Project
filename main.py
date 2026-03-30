

# PROJECT TITLE: LIBRARY MANAGEMENT SYSTEM
# 1. Display the books
# 2. Search the books
# 3. Exit

print("\n========== WELCOME TO GALE'S LIBRARY MANAGEMENT SYSTEM!!! ==========")

# ADDING THE BOOKS CATEGORY
# category = ["History", "Literature", "Science/Physics", "Business Management", "Computer Science", "Personal Development"]


# ADDING THE TITLE
bookTitle = ["The Philippine Revolution", 
             "Noli Me Tangere", 
             "A Nation in the Making", 
             "Philippine Folk Literature", 
             "An Anarchy of Families"]
            
print("[1] View the Book Section")
print("[2] Search Book")
choice = int(input("Enter a number [1-2]: "))

match choice:
    case 1:
        print("\nLIST OF THE BOOKS")
        count = 1
        for title in bookTitle:
            print(count, ".", title)
            count = count + 1
        
        exit = input("\nDo you want to exit? [Y/N]: ")
        while True:
            if exit == "Y":
                print("Thank you for using the Library Management System!")
                break
            elif exit == "N":
                print("Redirecting to the main menu...")
            else:
                print("Invalid input. Please enter only 'Y' or 'N'")
                exit = input("\nDo you want to exit? [Y/N]: ")         
    case 2:
        search_again = True
        while search_again:
            search = input("Search a book: ")
            
            count = 1
            found = False
            for title in bookTitle:
                if search.lower() in title.lower():
                    print(count, "." , title)
                    count+= 1
                    found = True
                
            if not found:
                print("Book is not found.")
            
            exit = input("Do you want to search again? [Y/N]: ")
            while True:
                if exit == 'Y':
                    search_again = True
                    break
                elif exit == "N":
                    print("Redirecting to the main menu...")
                    search_again = False
                    break
                else:
                    print("Invalid input. Please enter only 'Y' or 'N'")
                    exit = input("Do you want to search again? [Y/N]: ")
        

    

            



