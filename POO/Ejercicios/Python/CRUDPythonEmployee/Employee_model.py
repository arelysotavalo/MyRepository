class Employee:
    def __init__(self, id, name, hours_worked, total_pay):
        self.id = int(id)
        self.name = name
        self.hours_worked = float(hours_worked)
        self.total_pay = float(total_pay)
