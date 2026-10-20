package ec.edu.espe.employee.controller;
import ec.edu.espe.employee.model.Employee;
import ec.edu.espe.employee.model.EmployeeCrud;
import java.util.List;

/**
 *
 * @author Arelys
 */

public class EmployeeController {

    private final EmployeeCrud crud = new EmployeeCrud();
    private final double PAY_PER_HOUR = 5.50;

    public Employee add(String name, double hoursWorked) {
        double totalPay = hoursWorked * PAY_PER_HOUR;
        Employee emp = new Employee(0, name, hoursWorked, totalPay);
        crud.addEmployee(emp);
        return emp;
    }

    public List<Employee> getAll() {
        return crud.getAllEmployees();
    }

    public boolean edit(int id, String name, double hoursWorked) {
        double totalPay = hoursWorked * PAY_PER_HOUR;
        Employee updated = new Employee(id, name, hoursWorked, totalPay);
        return crud.editEmployee(id, updated);
    }

    public boolean delete(int id) {
        return crud.deleteEmployee(id);
    }
}

