package ec.edu.espe.student.model;
import java.util.List;

/**
 *
 * @author Arelys Otavalo
 */

public class Student {
    private int studentId;
    private String studentName;
    private List<Double> gradesList;
    private double averageGrade;

    public Student(int studentId, String studentName, List<Double> gradesList) {
        this.studentId = studentId;
        this.studentName = studentName;
        this.gradesList = gradesList;
        calculateAverage();
    }

    public void calculateAverage() {
        if (gradesList == null || gradesList.isEmpty()) {
            this.averageGrade = 0;
        } else {
            double sum = 0;
            for (double g : gradesList) sum += g;
            this.averageGrade = sum / gradesList.size();
        }
    }

    public int getStudentId() {
        return studentId;
    }

    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public List<Double> getGradesList() {
        return gradesList;
    }

    public void setGradesList(List<Double> gradesList) {
        this.gradesList = gradesList;
    }

    public double getAverageGrade() {
        return averageGrade;
    }

    public void setAverageGrade(double averageGrade) {
        this.averageGrade = averageGrade;
    }

    
}