class Employee {
    constructor(id, name, hoursWorked, totalPay) {
        this.id = Number(id);
        this.name = name;
        this.hoursWorked = Number(hoursWorked);
        this.totalPay = Number(totalPay);
    }
}

module.exports = Employee;
