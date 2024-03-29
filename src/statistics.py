from src.students import *


class Statistics(Students):

    def averageSubject(self, id_student, name_student, surname_student, name_subject):
        if self.keys.__contains__((str(id_student), name_student, surname_student)):
            keysSubjects = self.students[(str(id_student), name_student, surname_student)]["subjects"]
            if [*keysSubjects].__contains__(name_subject):
                valuesSubject = keysSubjects[name_subject].values()
                if valuesSubject:
                    return "average" + " " + name_subject, sum(valuesSubject) / len(valuesSubject)
                else:
                    raise Exception("Do_not_have_marks")
            else:
                raise Exception("Student_not_have_this_subject")
        else:
            raise Exception("There_is_not_such_student")

    def averageSubjects(self, id_student, name_student, surname_student):
        if self.keys.__contains__((str(id_student), name_student, surname_student)):
            values = list(self.students[(str(id_student), name_student, surname_student)]["subjects"].values())
            if not values:
                raise Exception("Do_not_have_subjects")
            else:
                for dictionary in list(values):
                    if not list(dictionary.values()):
                        values.remove(dictionary)
                if not values:
                    raise Exception("Do_not_have_marks")
                else:
                    for i in range(len(values)):
                        marksWithSubject = list(values[i].values())
                        values[i] = sum(marksWithSubject) / len(marksWithSubject)
                    return "average", sum(values) / len(values)
        else:
            raise Exception("There_is_not_such_student")
