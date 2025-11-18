from Employee_controller import EmployeeController

controller = EmployeeController()

def menu():
    while True:
        print("\n===== EMPLOYEE MENU =====")
        print("1. Show all employees")
        print("2. Add new employee")
        print("3. Edit employee")
        print("4. Delete employee")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            print("\n--- EMPLOYEE LIST ---")
            print(controller.get_all())

        elif option == "2":
            name = input("Employee name: ")
            hours = float(input("Hours worked: "))

            employee = controller.add(name, hours)
            print("\nEmployee added successfully!")
            print(employee.__dict__)

        elif option == "3":
            id = int(input("Enter employee ID to edit: "))
            name = input("New name: ")
            hours = float(input("New hours worked: "))

            success = controller.edit(id, name, hours)
            if success:
                print("\nEmployee updated successfully!")
            else:
                print("\nEmployee not found.")

        elif option == "4":
            id = int(input("Enter employee ID to delete: "))
            success = controller.delete(id)
            if success:
                print("\nEmployee deleted successfully!")
            else:
                print("\nEmployee not found.")

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()
