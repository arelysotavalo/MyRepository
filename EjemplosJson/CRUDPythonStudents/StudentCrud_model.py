import json
import os
from Student_model import Student

class StudentCrud:
    def __init__(self, file_path="students.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)

    def load_student_data(self):
        with open(self.file_path, "r") as file:
            student_data_list = json.load(file)
        return student_data_list

    def save_student_data(self, student_data_list):
        with open(self.file_path, "w") as file:
            json.dump(student_data_list, file, indent=4)

    def generate_student_id(self):
        student_data_list = self.load_student_data()
        if len(student_data_list) > 0:
            return student_data_list[-1]["student_id"] + 1
        else:
            return 1

    def add_student(self, student):
        student_data_list = self.load_student_data()
        student_data_list.append(student.__dict__)
        self.save_student_data(student_data_list)

    def get_all_students(self):
        student_data_list = self.load_student_data()
        student_list = []
        for student_data in student_data_list:
            student_object = Student(student_data["student_id"], student_data["student_name"], student_data["grades_list"])
            student_list.append(student_object)
        return student_list

    def edit_student(self, student_id, new_student_name, new_grades_list):
        student_data_list = self.load_student_data()
        for student_data in student_data_list:
            if student_data["student_id"] == student_id:
                if new_student_name != "":
                    student_data["student_name"] = new_student_name
                if len(new_grades_list) > 0:
                    student_data["grades_list"] = new_grades_list
                self.save_student_data(student_data_list)
                return True
        return False

    def delete_student(self, student_id):
        student_data_list = self.load_student_data()
        updated_student_data_list = [student_data for student_data in student_data_list if student_data["student_id"] != student_id]
        if len(updated_student_data_list) != len(student_data_list):
            self.save_student_data(updated_student_data_list)
            return True
        return False


#30  student_data_list.append(student.__dict__)
#student_data_list.append({
    #"student_id": student.student_id,
    #"student_name": student.student_name,
   # "grades_list": student.grades_list
#}) 
#No average in json