from src.students import *


class Subjects(Students):

    def addSubject(self, id, name_student, surname_student, name_subject):
        if type(name_subject) != str:
            raise TypeError("Bad_type_subject_name")
