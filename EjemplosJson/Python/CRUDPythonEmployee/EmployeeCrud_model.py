import json
import os
from Employee_model import Employee

class EmployeeCrud:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "employees.json")

        # Crear el archivo JSON si no existe
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

    def load_data(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def generate_id(self):
        data = self.load_data()
        if len(data) > 0:
            return data[-1]["id"] + 1
        else:
            return 1

    def add_employee(self, employee):
        data = self.load_data()
        employee.id = self.generate_id()
        data.append(employee.__dict__)
        self.save_data(data)

    def get_all_employees(self):
        return self.load_data()

    def edit_employee(self, id, updated_employee):
        data = self.load_data()
        for i, emp in enumerate(data):
            if emp["id"] == id:
                updated_employee.id = id
                data[i] = updated_employee.__dict__
                self.save_data(data)
                return True
        return False

    def delete_employee(self, id):
        data = self.load_data()
        new_data = [emp for emp in data if emp["id"] != id]
        if len(new_data) != len(data):
            self.save_data(new_data)
            return True
        return False
