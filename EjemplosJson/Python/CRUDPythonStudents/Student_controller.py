from StudentCrud_model import StudentCrud
from Student_model import Student

class StudentController:
    def __init__(self):
        self.student_crud = StudentCrud()

    def add_student(self, student_name, grades_list):
        student_id = self.student_crud.generate_student_id()
        student_object = Student(student_id, student_name, grades_list)
        self.student_crud.add_student(student_object)
        return student_object

    def get_all_students(self):
        return self.student_crud.get_all_students()

    def edit_student(self, student_id, new_student_name, new_grades_list):
        return self.student_crud.edit_student(student_id, new_student_name, new_grades_list)

    def delete_student(self, student_id):
        return self.student_crud.delete_student(student_id)
