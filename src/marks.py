from src.students import *


class Marks(Students):

    def addMark(self, id, name_student, surname_student, name_subject, name_mark, grade):
        if type(grade) != int:
            raise TypeError("Bad_type_grade")
        elif grade > 6 or grade < 1:
            raise Exception("Bad_range_marks")
        else:
            if self.keys.__contains__((str(id), name_student, surname_student)):
                valueSubjects = self.students[(str(id), name_student, surname_student)]["subjects"]
                if [*valueSubjects].__contains__(name_subject):
                    if [*valueSubjects[name_subject]].__contains__(name_mark):
                        raise Exception("This_mark_already_exists")
                    else:
                        valueSubjects[name_subject][name_mark] = grade
                        return list(valueSubjects[name_subject].items())
                else:
                    raise Exception("Student_not_have_this_subject")
            else:
                raise Exception("There_is_not_such_student")
