const StudentCrud = require("../Model/StudentCrud");
const Student = require("../Model/Student");

class StudentController {
    constructor() {
        this.studentCrud = new StudentCrud();
    }

    addStudent(studentName, gradesList) {
        const newStudentId = this.studentCrud.generateStudentId();
        const newStudent = new Student(newStudentId, studentName, gradesList);
        this.studentCrud.addStudent(newStudent);
        return newStudent;
    }

    getAllStudents() {
        return this.studentCrud.getAllStudents();
    }

    editStudent(studentId, newStudentName, newGradesList) {
        return this.studentCrud.editStudent(studentId, newStudentName, newGradesList);
    }

    deleteStudent(studentId) {
        return this.studentCrud.deleteStudent(studentId);
    }
}

module.exports = StudentController;
