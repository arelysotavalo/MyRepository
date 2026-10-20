package ec.edu.espe.employee.model;

/**
 *
 * @author Arelys
 */

public class Employee {
    private int id;
    private String name;
    private double hoursWorked;
    private double totalPay;

    public Employee(int id, String name, double hoursWorked, double totalPay) {
        this.id = id;
        this.name = name;
        this.hoursWorked = hoursWorked;
        this.totalPay = totalPay;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public double getHoursWorked() { return hoursWorked; }
    public double getTotalPay() { return totalPay; }

    public void setId(int id) { this.id = id; }
    public void setName(String name) { this.name = name; }
    public void setHoursWorked(double hoursWorked) { this.hoursWorked = hoursWorked; }
    public void setTotalPay(double totalPay) { this.totalPay = totalPay; }
}

