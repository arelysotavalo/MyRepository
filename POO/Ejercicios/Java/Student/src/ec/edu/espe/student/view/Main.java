package ec.edu.espe.student.view;

import ec.edu.espe.student.controller.StudentController;
import ec.edu.espe.student.model.Student;
import java.util.*;

/**
 *
 * @author Arelys
 */
public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final StudentController controller = new StudentController();

    public static void main(String[] args) {
        menu();
    }

    private static void menu() {
        System.out.println("\n===== STUDENT MENU =====");
        System.out.println("1. Show all students");
        System.out.println("2. Add new student");
        System.out.println("3. Edit student");
        System.out.println("4. Delete student");
        System.out.println("5. Exit");
        System.out.print("Choose an option: ");

        String choice = scanner.nextLine();

        switch (choice) {
            case "1" ->
                showStudents();
            case "2" ->
                addStudent();
            case "3" ->
                editStudent();
            case "4" ->
                deleteStudent();
            case "5" ->
                System.exit(0);
            default ->
                menu();
        }
    }

    private static void showStudents() {
        List<Student> students = controller.getAllStudents();

        for (Student s : students) {
            System.out.println(
                    "ID: " + s.getStudentId()
                    + ", Name: " + s.getStudentName()
                    + ", Grades: " + s.getGradesList()
                    + ", Average: " + s.getAverageGrade()
            );
        }
        menu();
    }

    private static void addStudent() {
        System.out.print("Student name: ");
        String name = scanner.nextLine();

        List<Double> grades = new ArrayList<>();

        for (int i = 1; i <= 5; i++) {
            while (true) {
                try {
                    System.out.print("Enter grade #" + i + " (0 to 20): ");
                    double grade = Double.parseDouble(scanner.nextLine());

                    if (grade >= 0 && grade <= 20) {
                        grades.add(grade);
                        break; 
                    } else {
                        System.out.println(" Grade must be between 0 and 20. Try again.");
                    }

                } catch (NumberFormatException e) {
                    System.out.println(" Invalid input. Enter a valid number.");
                }
            }
        }

        Student student = controller.addStudent(name, grades);
        System.out.println("Student added: ID " + student.getStudentId());

        menu();
    }

    private static void editStudent() {
        System.out.print("Enter student ID to edit: ");
        int id = Integer.parseInt(scanner.nextLine());

        System.out.print("New name (leave blank): ");
        String name = scanner.nextLine();

        List<Double> grades = new ArrayList<>();
        for (int i = 1; i <= 5; i++) {
            System.out.print("Enter new grade #" + i + " (leave blank): ");
            String input = scanner.nextLine();
            if (!input.isEmpty()) {
                grades.add(Double.parseDouble(input));
            }
        }

        if (controller.editStudent(id, name, grades)) {
            System.out.println("Student updated!");
        } else {
            System.out.println("Student not found.");
        }

        menu();
    }

    private static void deleteStudent() {
        System.out.print("Enter student ID to delete: ");
        int id = Integer.parseInt(scanner.nextLine());

        if (controller.deleteStudent(id)) {
            System.out.println("Student deleted.");
        } else {
            System.out.println("Student not found.");
        }

        menu();
    }
}



// 65    List<Double> grades = new ArrayList<>();
//
// while (true) {
//     System.out.print("Enter grade (leave blank to finish): ");
//     String input = scanner.nextLine().trim();
//
//     if (input.isEmpty()) {
//         break;
//     }
//
//     try {
//         double grade = Double.parseDouble(input);
//         if (grade >= 0 && grade <= 20) {
//             grades.add(grade);
//         } else {
//             System.out.println("Grade must be between 0 and 20.");
//         }
//
//     } catch (NumberFormatException e) {
//         System.out.println("Invalid number. Try again.");
//     }
// }
