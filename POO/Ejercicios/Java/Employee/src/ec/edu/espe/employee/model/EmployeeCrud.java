package ec.edu.espe.employee.model;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;


/**
 *
 * @author Arelys
 */

public class EmployeeCrud {

    private final String FILE_PATH = "employeesJava.json";
    private final Gson gson = new Gson();

    public EmployeeCrud() {
        File f = new File(FILE_PATH);
        try {
            if (!f.exists()) {
                f.createNewFile();
                saveData(new ArrayList<>());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private List<Employee> loadData() {
        try (Reader r = new FileReader(FILE_PATH)) {
            Type listType = new TypeToken<List<Employee>>() {}.getType();
            List<Employee> list = gson.fromJson(r, listType);
            return list != null ? list : new ArrayList<>();
        } catch (IOException e) {
            return new ArrayList<>();
        }
    }

    private void saveData(List<Employee> data) {
        try (Writer writer = new FileWriter(FILE_PATH)) {
            gson.toJson(data, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public int generateId() {
        List<Employee> data = loadData();
        return data.size() > 0 ? data.get(data.size() - 1).getId() + 1 : 1;
    }

    public void addEmployee(Employee employee) {
        List<Employee> data = loadData();
        employee.setId(generateId());
        data.add(employee);
        saveData(data);
    }

    public List<Employee> getAllEmployees() {
        return loadData();
    }

    public boolean editEmployee(int id, Employee updated) {
        List<Employee> data = loadData();

        for (int i = 0; i < data.size(); i++) {
            if (data.get(i).getId() == id) {
                updated.setId(id);
                data.set(i, updated);
                saveData(data);
                return true;
            }
        }
        return false;
    }

    public boolean deleteEmployee(int id) {
        List<Employee> data = loadData();
        int before = data.size();

        data.removeIf(emp -> emp.getId() == id);

        if (data.size() != before) {
            saveData(data);
            return true;
        }

        return false;
    }
}

