# This program creates a dictionary where: Keys = student names, Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) depending on the operation they want to perform on the dictionary:
# A - Add a student, B - Update marks, C - Search for a student, D - Display all students and marks

student_dict = {}

while True:
    print("Menu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")
    
    choice = input("Enter your choice: ").upper()
    
    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student_dict[name] = marks
        print(f"Student {name} added with marks {marks}.")
        
    elif choice == 'B':
        name = input("Enter student name to update marks: ")
        if name in student_dict:
            marks = int(input("Enter new marks: "))
            student_dict[name] = marks
            print(f"Marks for {name} updated to {marks}.")
        else:
            print(f"Student {name} not found.")
            
    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in student_dict:
            print(f"{name} has marks: {student_dict[name]}")
        else:
            print(f"Student {name} not found.")
            
    elif choice == 'D':
        print("All students and their marks:")
        for name, marks in student_dict.items():
            print(f"{name}: {marks}")
            
    elif choice == 'E':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")