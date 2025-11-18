package ec.edu.espe.student.controller;
import ec.edu.espe.student.model.Student;
import ec.edu.espe.student.model.StudentCrud;

/**
 *
 * @author Arelys
 */

import java.util.List;

public class StudentController {
    private final StudentCrud crud;

    public StudentController() {
        crud = new StudentCrud();
    }

    public Student addStudent(String name, List<Double> grades) {
        int id = crud.generateStudentId();
        Student student = new Student(id, name, grades);
        crud.addStudent(student);
        return student;
    }

    public List<Student> getAllStudents() {
        return crud.getAllStudents();
    }

    public boolean editStudent(int id, String newName, List<Double> newGrades) {
        return crud.editStudent(id, newName, newGrades);
    }

    public boolean deleteStudent(int id) {
        return crud.deleteStudent(id);
    }
}
