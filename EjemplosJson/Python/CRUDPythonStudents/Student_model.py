class Student:
    def __init__(self, student_id, student_name, grades_list):
        self.student_id = student_id
        self.student_name = student_name
        self.grades_list = grades_list if grades_list != [] else []
        self.average_grade = self.calculate_average()

    def calculate_average(self):
        if len(self.grades_list) == 0:
            return 0
        return sum(self.grades_list) / len(self.grades_list)


#Without avarege in json: 
#class Student:
   # def __init__(self, student_id, student_name, grades_list):
        #self.student_id = student_id
        #self.student_name = student_name
        #self.grades_list = grades_list if grades_list != [] else []

   # def calculate_average(self):
       # if len(self.grades_list) == 0:
           # return 0
       # return sum(self.grades_list) / len(self.grades_list)