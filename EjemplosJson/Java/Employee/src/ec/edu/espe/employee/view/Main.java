package ec.edu.espe.employee.view;
import ec.edu.espe.employee.controller.EmployeeController;
import ec.edu.espe.employee.model.Employee;
import java.util.List;
import java.util.Scanner;
/**
 *
 * @author Arelys
 */

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        EmployeeController controller = new EmployeeController();

        while (true) {
            System.out.println("\n===== EMPLOYEE MENU =====");
            System.out.println("1. Show all employees");
            System.out.println("2. Add new employee");
            System.out.println("3. Edit employee");
            System.out.println("4. Delete employee");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            String option = scanner.nextLine();

            switch (option) {

                case "1":
                    List<Employee> employees = controller.getAll();
                    employees.forEach(emp -> System.out.println(
                            "ID: " + emp.getId() +
                            ", Name: " + emp.getName() +
                            ", Hours: " + emp.getHoursWorked() +
                            ", Total Pay: " + emp.getTotalPay()
                    ));
                    break;

                case "2":
                    System.out.print("Employee name: ");
                    String name = scanner.nextLine();

                    System.out.print("Hours worked: ");
                    double hours = Double.parseDouble(scanner.nextLine());

                    Employee emp = controller.add(name, hours);
                    System.out.println("Employee added. ID = " + emp.getId());
                    break;

                case "3":
                    System.out.print("Enter ID to edit: ");
                    int editId = Integer.parseInt(scanner.nextLine());

                    System.out.print("New name: ");
                    String newName = scanner.nextLine();

                    System.out.print("New hours worked: ");
                    double newHours = Double.parseDouble(scanner.nextLine());

                    if (controller.edit(editId, newName, newHours)) {
                        System.out.println("Employee updated.");
                    } else {
                        System.out.println("Employee not found.");
                    }
                    break;

                case "4":
                    System.out.print("Enter ID to delete: ");
                    int delId = Integer.parseInt(scanner.nextLine());

                    if (controller.delete(delId)) {
                        System.out.println("Employee deleted.");
                    } else {
                        System.out.println("Employee not found.");
                    }
                    break;

                case "5":
                    System.out.println("Goodbye!");
                    return;

                default:
                    System.out.println("Invalid option.");
            }
        }
    }
}

