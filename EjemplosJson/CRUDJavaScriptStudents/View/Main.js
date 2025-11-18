const readline = require("readline");
const StudentController = require("../Controller/StudentController");
const Student = require("../Model/Student");

const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const studentController = new StudentController();

function menu() {
    console.log("\n===== STUDENT MENU =====");
    console.log("1. Show all students");
    console.log("2. Add new student");
    console.log("3. Edit student");
    console.log("4. Delete student");
    console.log("5. Exit");

    reader.question("Choose an option: ", (selectedOption) => {
        switch(selectedOption) {
            case "1":
                console.log("\n--- Student List ---");
                const studentList = studentController.getAllStudents();
                studentList.forEach(student => {
                    console.log(`ID: ${student.student_id}, Name: ${student.student_name}, Grades: ${student.grades_list}, Average: ${student.average_grade.toFixed(2)}`);
                });
                menu();
                break;

            case "2":
                reader.question("Student name: ", (studentName) => {
                    const gradesList = [];
                    const totalGrades = 5; // HOW MANY GRADES 

                    function askGrade(index) {
                        if (index < totalGrades) {
                            reader.question(`Enter grade ${index + 1} (0-20): `, (gradeInput) => {
                                const gradeValue = parseFloat(gradeInput.trim());
                                if (!isNaN(gradeValue) && gradeValue >= 0 && gradeValue <= 20) {
                                    gradesList.push(gradeValue);
                                    askGrade(index + 1); // NEXT GRADE
                                } else {
                                    console.log("Invalid grade. Please enter a value between 0 and 20.");
                                    askGrade(index); // Repeat the same grade
                                }
                            });
                        } else {
                            // All grades entered
                            const studentObject = studentController.addStudent(studentName, gradesList);
                            console.log(`The student record was successfully added. ID: ${studentObject.student_id}, Average grade: ${studentObject.average_grade.toFixed(2)}`);
                            menu();
                        }
                    }

                    askGrade(0); // Start with the first grade
                });
                break;

            case "3":
                reader.question("Enter the ID of the student you want to edit: ", (studentIdInput) => {
                    const studentId = parseInt(studentIdInput);

                    reader.question("New name (leave blank to keep current): ", (newStudentName) => {
                        const newGradesList = [];
                        const totalGrades = 5; // HOW MANY GRADES TO EDIT

                        function askNewGrade(index) {
                            if (index < totalGrades) {
                                reader.question(`Enter new grade ${index + 1} (0-20, leave blank to keep current): `, (gradeInput) => {
                                    if (gradeInput.trim() === "") {
                                        askNewGrade(index + 1); // Keep current grade
                                    } else {
                                        const gradeValue = parseFloat(gradeInput.trim());
                                        if (!isNaN(gradeValue) && gradeValue >= 0 && gradeValue <= 20) {
                                            newGradesList.push(gradeValue);
                                            askNewGrade(index + 1);
                                        } else {
                                            console.log("Invalid grade. Please enter a value between 0 and 20.");
                                            askNewGrade(index); // Repeat the same grade
                                        }
                                    }
                                });
                            } else {
                                const updateSuccess = studentController.editStudent(studentId, newStudentName, newGradesList);
                                console.log(updateSuccess ? "The student record was successfully updated." : "No student was found with the specified ID.");
                                menu();
                            }
                        }

                        askNewGrade(0);
                    });
                });
                break;

            case "4":
                reader.question("Enter the ID of the student you want to delete: ", (studentIdInput) => {
                    const studentId = parseInt(studentIdInput);
                    const deleteSuccess = studentController.deleteStudent(studentId);

                    console.log(deleteSuccess ? "The student record was successfully deleted." : "No student was found with the specified ID.");
                    menu();
                });
                break;

            case "5":
                console.log("Goodbye! Exiting the program.");
                reader.close();
                break;

            default:
                console.log("Invalid option. Please select a valid option from the menu.");
                menu();
        }
    });
}

menu();
