# Student Record System
# 1. add student
# 2. displat all students

students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = int(input("Choose [1-3]: "))
    
    match(choice):
        case 1:
            name = input("Enter a student name: ")
            students.append(name)
        case 2:
            if students:
                for count, student in enumerate(students, 1):
                    print(f"{count}. {student}")
            else:
                print("No students added yet.")
        case 3:
            print("Exiting program...")
            break  
        case _:
            print("Invalid input.Try again")
              
            