class Student {
    constructor(studentId, studentName, gradesList) {
        this.student_id = Number(studentId);
        this.student_name = studentName;
        // Validación de notas: solo se guardan entre 0 y 20
        this.grades_list = (gradesList && gradesList.length > 0) 
            ? gradesList.filter(grade => grade >= 0 && grade <= 20) 
            : [];
        this.average_grade = this.calculateAverage();
    }

    calculateAverage() {
        if (this.grades_list.length === 0) {
            return 0;
        }
        const sumOfGrades = this.grades_list.reduce((total, grade) => total + grade, 0);
        return sumOfGrades / this.grades_list.length;
    }
}

module.exports = Student;


/*
No average in json
    student_id: student.student_id,
    student_name: student.student_name,
    grades_list: student.grades_list
});
De esta forma, 'average_grade' no se escribe en el archivo, pero sigue existiendo en el objeto.
*/
