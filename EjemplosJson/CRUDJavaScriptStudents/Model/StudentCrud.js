const fs = require("fs");
const path = require("path");
const Student = require("../Model/Student");

class StudentCrud {
    constructor(filePath = path.join(__dirname, "students.json")) {
        this.filePath = filePath;

        if (!fs.existsSync(this.filePath)) {
            fs.writeFileSync(this.filePath, JSON.stringify([]), "utf8");
        }
    }

    loadStudentData() {
        const data = fs.readFileSync(this.filePath, "utf8");
        return JSON.parse(data);
    }

    saveStudentData(studentDataList) {
        fs.writeFileSync(this.filePath, JSON.stringify(studentDataList, null, 4), "utf8");
    }

    generateStudentId() {
        const studentDataList = this.loadStudentData();
        if (studentDataList.length > 0) {
            return studentDataList[studentDataList.length - 1].student_id + 1;
        } else {
            return 1;
        }
    }

    addStudent(student) {
        const studentDataList = this.loadStudentData();
        studentDataList.push(student);
        this.saveStudentData(studentDataList);
    }

    getAllStudents() {
        const studentDataList = this.loadStudentData();
        return studentDataList.map(sd => new Student(sd.student_id, sd.student_name, sd.grades_list));
    }

    editStudent(studentId, newStudentName, newGradesList) {
        const studentDataList = this.loadStudentData();
        let updated = false;

        for (let studentData of studentDataList) {
            if (studentData.student_id === studentId) {
                if (newStudentName !== "") studentData.student_name = newStudentName;
                if (newGradesList.length > 0) studentData.grades_list = newGradesList;
                updated = true;
                break;
            }
        }

        if (updated) this.saveStudentData(studentDataList);
        return updated;
    }

    deleteStudent(studentId) {
        const studentDataList = this.loadStudentData();
        const updatedStudentDataList = studentDataList.filter(sd => sd.student_id !== studentId);

        if (updatedStudentDataList.length !== studentDataList.length) {
            this.saveStudentData(updatedStudentDataList);
            return true;
        }
        return false;
    }
}

module.exports = StudentCrud;


//34 studentDataList.push({
    //student_id: student.student_id,
    //student_name: student.student_name,
    //grades_list: student.grades_list
//});
