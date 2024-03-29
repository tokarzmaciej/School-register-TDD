from src.students import *


class Subjects(Students):

    def addSubject(self, id_student, name_student, surname_student, name_subject):
        if type(name_subject) != str:
            raise TypeError("Bad_type_subject_name")
        else:
            if self.keys.__contains__((str(id_student), name_student, surname_student)):
                self.students[(str(id_student), name_student, surname_student)]["subjects"][name_subject] = {}

                return self.students[(str(id_student), name_student, surname_student)]
            else:
                raise Exception("There_is_not_such_student")

    def deleteSubject(self, id_student, name_student, surname_student, name_subject):
        if type(name_subject) != str:
            raise TypeError("Bad_type_subject_name")
        else:
            if self.keys.__contains__((str(id_student), name_student, surname_student)):
                valuesSubject = self.students[(str(id_student), name_student, surname_student)]["subjects"]
                if [*valuesSubject].__contains__(name_subject):
                    valuesSubject.pop(name_subject)
                    return self.students[(str(id_student), name_student, surname_student)]
                else:
                    raise Exception("Student_not_have_this_subject")
            else:
                raise Exception("There_is_not_such_student")

    def editSubject(self, id_student, name_student, surname_student, name_subject, new_name_subject):
        if type(new_name_subject) != str:
            raise TypeError("Bad_type_new_subject_name")
        else:
            if self.keys.__contains__((str(id_student), name_student, surname_student)):
                valuesSubject = self.students[(str(id_student), name_student, surname_student)]["subjects"]
                if [*valuesSubject].__contains__(name_subject):
                    valuesSubject[new_name_subject] = valuesSubject.pop(name_subject)
                    return [*valuesSubject]
                else:
                    raise Exception("Student_not_have_this_subject")

            else:
                raise Exception("There_is_not_such_student")
