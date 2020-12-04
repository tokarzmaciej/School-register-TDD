from src.students import *


class Marks(Students):

    def addMark(self, id, name_student, surname_student, name_subject, name_mark, grade):
        if type(grade) != int:
            raise TypeError("Bad_type_grade")
        elif grade > 6 or grade < 1:
            raise Exception("Bad_range_marks")
