const fs = require("fs");
const path = require("path");

class EmployeeCrud {

    constructor() {
        this.filePath = path.join(__dirname, "employees.json");

        // Create the JSON file if it doesn't exist
        if (!fs.existsSync(this.filePath)) {
            fs.writeFileSync(this.filePath, JSON.stringify([]), "utf8");
        }
    }

    loadData() {
        const jsonData = fs.readFileSync(this.filePath, "utf8");
        return JSON.parse(jsonData);
    }

    saveData(data) {
        fs.writeFileSync(this.filePath, JSON.stringify(data, null, 4), "utf8");
    }

    generateId() {
        const data = this.loadData();
        return data.length > 0 ? data[data.length - 1].id + 1 : 1;
    }

    addEmployee(employee) {
        const data = this.loadData();
        employee.id = this.generateId(); 
        data.push(employee);
        this.saveData(data);
    }

    getAllEmployees() {
        return this.loadData();
    }


    editEmployee(id, updatedEmployee) {
        const data = this.loadData();
        const index = data.findIndex(emp => emp.id === id);

        if (index !== -1) {
            updatedEmployee.id = id;
            data[index] = updatedEmployee;
            this.saveData(data);
            return true; 
        } else {
            return false; 
        }
    }

    deleteEmployee(id) {
        const data = this.loadData();
        const newData = data.filter(emp => emp.id !== id);

        if (newData.length !== data.length) {
            this.saveData(newData);
            return true; 
        } else {
            return false; 
        }
    }
}

module.exports = EmployeeCrud;
