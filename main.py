

# PROJECT TITLE: LIBRARY MANAGEMENT SYSTEM
# 1. Login to the system
# 2. View the books
# 3. Search the books
# 4. Logout

# ADDING FEATURES IN THE SYSTEM
# 1. add a database to save the already registered users
# 2. add a category in the book section
# 3. add a remove and add to cart in the book menu
# 

# ADDING THE TITLE
bookTitle = ["The Philippine Revolution", 
             "Noli Me Tangere", 
             "A Nation in the Making", 
             "Philippine Folk Literature", 
             "An Anarchy of Families"]

# Store registered users
users = {}


def display_books():
    """Display all books in the library."""
    print("\n========== LIST OF THE BOOKS ==========")
    for count, title in enumerate(bookTitle, 1):
        print(f"{count}. {title}")


def search_books():
    """Search for books by keyword."""
    while True:
        search_term = input("\nSearch a book: ")
        
        count = 1
        found = False
        for title in bookTitle:
            if search_term.lower() in title.lower():
                print(f"{count}. {title}")
                count += 1
                found = True
        
        if not found:
            print("Book is not found.")
        
        search_again = input("\nDo you want to search again? [Y/N]: ").upper()
        while search_again not in ['Y', 'N']:
            print("Invalid input. Please enter only 'Y' or 'N'")
            search_again = input("Do you want to search again? [Y/N]: ").upper()
        
        if search_again == 'N':
            break


def register():
    """Register a new user."""
    print("\n========== REGISTER ==========")
    username = input("Enter username: ")
    
    if username in users:
        print("Username already exists! Please try another.")
        return False
    
    password = input("Enter password: ")
    users[username] = password
    print(f"Welcome {username}! You have been registered successfully!")
    return True


def login():
    """Login an existing user."""
    print("\n========== LOGIN ==========")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid username or password!")
        return None


def book_menu(username):
    """Display book menu for logged-in users."""
    while True:
        print(f"\n========== BOOK MENU (User: {username}) ==========")
        print("[1] View the Book Section")
        print("[2] Search Book")
        print("[3] Logout")
        
        choice = input("Enter a number [1-3]: ")
        
        match choice:
            case "1":
                display_books()
            case "2":
                search_books()
            case "3":
                print(f"Thank you for using the Library Management System, {username}!")
                return False
            case _:
                print("Invalid input. Please enter between [1-3]")


def main_menu():
    """Main menu for the library system."""
    while True:
        print("\n========== WELCOME TO GALE'S LIBRARY MANAGEMENT SYSTEM!!! ==========")
        print("[1] Register")
        print("[2] Login")
        print("[3] Exit")
        
        choice = input("Enter a number [1-3]: ")
        
        match choice:
            case "1":
                register()
            case "2":
                username = login()
                if username:
                    book_menu(username)
            case "3":
                print("Thank you for visiting Gale's Library Management System!")
                break
            case _:
                print("Invalid input. Please enter 1, 2, or 3")


# Run the program
if __name__ == "__main__":
    main_menu()
        

    

            



