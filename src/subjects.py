from src.students import *


class Subjects(Students):

    def addSubject(self, id, name_student, surname_student, name_subject):
        keys = [*self.students]
        if type(name_subject) != str:
            raise TypeError("Bad_type_subject_name")
        else:
            raise Exception("There_is_not_such_student")

