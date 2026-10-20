from Student_controller import StudentController

student_controller = StudentController()

def menu():
    print("\n===== STUDENT MENU =====")
    print("1. Show all students")
    print("2. Add new student")
    print("3. Edit student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        student_list = student_controller.get_all_students()
        for student in student_list:
            print(f"ID: {student.student_id}, Name: {student.student_name}, Grades: {student.grades_list}, Average: {student.average_grade:.2f}")
        menu()

    elif choice == "2":
        student_name = input("Student name: ")

        # NUMBER OF GRADES
        number_of_grades = 5  
        grades_list = []

        #Every grade one by one 
        for i in range(number_of_grades):
            while True:
                try:
                    grade = float(input(f"Enter grade #{i+1} (between 0 and 20): "))
                    if 0 <= grade <= 20:
                        grades_list.append(grade)
                        break
                    else:
                        print("Grade must be between 0 and 20. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number.")

        # create students with grades
        student_object = student_controller.add_student(student_name, grades_list)
        print(f"Student added: ID {student_object.student_id}, Average {student_object.average_grade:.2f}")
        menu()

    elif choice == "3":
        student_id = int(input("Enter student ID to edit: "))
        new_student_name = input("New name (leave blank to keep current): ").strip()

        number_of_grades = 5  # number of grades
        new_grades_list = []

        # Every grade one by one 
        for i in range(number_of_grades):
            while True:
                grades_input = input(f"Enter new grade #{i+1} (leave blank to keep current): ").strip()
                if grades_input == "":
                    break  
                try:
                    grade = float(grades_input)
                    if 0 <= grade <= 20:
                        new_grades_list.append(grade)
                        break
                    else:
                        print("Grade must be between 0 and 20. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number.")

        success = student_controller.edit_student(student_id, new_student_name, new_grades_list)
        if success:
            print("Student updated successfully!")
        else:
            print("Student not found.")
        menu()

    elif choice == "4":
        student_id = int(input("Enter student ID to delete: "))
        success = student_controller.delete_student(student_id)
        if success:
            print("Student deleted successfully!")
        else:
            print("Student not found.")
        menu()

    elif choice == "5":
        print("Goodbye!")
        exit()

    else:
        print("Invalid option")
        menu()

menu()
