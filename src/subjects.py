from src.students import *


class Subjects(Students):

    def addSubject(self, id, name_student, surname_student, name_subject):
        if type(name_subject) != str:
            raise TypeError("Bad_type_subject_name")
        else:
            if self.keys.__contains__((str(id), name_student, surname_student)):
                self.students[(str(id), name_student, surname_student)]["subjects"][name_subject] = {}

                return self.students[(str(id), name_student, surname_student)]
            else:
                raise Exception("There_is_not_such_student")

    def deleteSubject(self, id, name_student, surname_student, name_subject):
        if type(name_subject) != str:
            raise TypeError("Bad_type_subject_name")
        else:
            if not self.keys.__contains__((str(id), name_student, surname_student)):
                raise Exception("There_is_not_such_student")
            else:
                if not [*self.students[(str(id), name_student, surname_student)]["subjects"]].__contains__(
                        name_subject):
                    raise Exception("Student_not_have_this_subject")
                else:
                    self.students[(str(id), name_student, surname_student)]["subjects"].pop(name_subject)
                    return self.students[(str(id), name_student, surname_student)]
