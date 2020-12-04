from src.students import *


class Subjects(Students):

    def addSubject(self, id, name_student, surname_student, name_subject):
        keys = [*self.students]
        if type(name_subject) != str:
            raise TypeError("Bad_type_subject_name")
        else:
            if keys.__contains__((str(id), name_student, surname_student)):
                self.students[(str(id), name_student, surname_student)]["subjects"][name_subject] = {}

                return self.students[(str(id), name_student, surname_student)]
            else:
                raise Exception("There_is_not_such_student")

    def deleteSubject(self, id, name_student, surname_student, name_subject):
        raise TypeError("Bad_type_subject_name")