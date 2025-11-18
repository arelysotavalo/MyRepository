const EmployeeCrud = require("../Model/EmployeeCrud");
const Employee = require("../Model/Employee");

class EmployeeController {

    constructor() {
        this.crud = new EmployeeCrud();
        this.payPerHour = 5.50; //PRICE FOR HOUR 
    }

    add(name, hoursWorked) {
        const id = this.crud.generateId();
        const totalPay = Number(hoursWorked) * this.payPerHour;
        const employee = new Employee(id, name, hoursWorked, totalPay);
        this.crud.addEmployee(employee);
        return employee;
    }

    getAll() {
        return this.crud.getAllEmployees();
    }


    edit(id, name, hoursWorked) {
        const totalPay = Number(hoursWorked) * this.payPerHour;
        const updatedEmployee = new Employee(id, name, hoursWorked, totalPay);
        const success = this.crud.editEmployee(id, updatedEmployee);
        return success; 
    }

    delete(id) {
        const success = this.crud.deleteEmployee(id);
        return success; 
    }
}

module.exports = EmployeeController;
