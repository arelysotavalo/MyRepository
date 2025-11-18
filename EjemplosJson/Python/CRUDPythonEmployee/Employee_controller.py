from EmployeeCrud_model import EmployeeCrud
from Employee_model import Employee

class EmployeeController:
    def __init__(self):
        self.crud = EmployeeCrud()
        self.pay_per_hour = 5.50  # PRICE FOR HOUR

    def add(self, name, hours_worked):
        id = self.crud.generate_id()
        total_pay = float(hours_worked) * self.pay_per_hour
        employee = Employee(id, name, hours_worked, total_pay)
        self.crud.add_employee(employee)
        return employee

    def get_all(self):
        return self.crud.get_all_employees()

    def edit(self, id, name, hours_worked):
        total_pay = float(hours_worked) * self.pay_per_hour
        updated_employee = Employee(id, name, hours_worked, total_pay)
        success = self.crud.edit_employee(id, updated_employee)
        return success

    def delete(self, id):
        success = self.crud.delete_employee(id)
        return success
