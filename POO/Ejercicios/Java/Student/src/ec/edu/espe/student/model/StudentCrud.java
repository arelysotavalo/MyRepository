package ec.edu.espe.student.model;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;


/**
 *
 * @author Arelys
 */


public class StudentCrud {

    private final String filePath = "studentsJava.json";
    private final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public StudentCrud() {
        File file = new File(filePath);
        try {
            if (!file.exists()) {
                FileWriter fw = new FileWriter(filePath);
                fw.write("[]");
                fw.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private List<Student> loadStudentData() {
        try {
            Reader reader = new FileReader(filePath);
            Type listType = new TypeToken<List<Student>>() {}.getType();
            List<Student> students = gson.fromJson(reader, listType);

            reader.close();

            return students != null ? students : new ArrayList<>();

        } catch (Exception e) {
            return new ArrayList<>();
        }
    }

    private void saveStudentData(List<Student> students) {
        try {
            Writer writer = new FileWriter(filePath);
            gson.toJson(students, writer);
            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public int generateStudentId() {
        List<Student> students = loadStudentData();
        if (students.isEmpty()) return 1;

        return students.get(students.size() - 1).getStudentId() + 1;
    }

    public void addStudent(Student student) {
        List<Student> students = loadStudentData();
        students.add(student);
        saveStudentData(students);
    }

    public List<Student> getAllStudents() {
        return loadStudentData();
    }

    public boolean editStudent(int id, String newName, List<Double> newGrades) {
        List<Student> students = loadStudentData();

        for (Student s : students) {
            if (s.getStudentId() == id) {

                if (!newName.isEmpty())
                    s.setStudentName(newName);

                if (!newGrades.isEmpty())
                    s.setGradesList(newGrades);

                saveStudentData(students);
                return true;
            }
        }

        return false;
    }

    public boolean deleteStudent(int id) {
        List<Student> students = loadStudentData();
        boolean removed = students.removeIf(s -> s.getStudentId() == id);

        if (removed) {
            saveStudentData(students);
        }

        return removed;
    }
}
