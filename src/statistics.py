from src.students import *


class Statistics(Students):

    def averageSubject(self, id, name_student, surname_student, name_subject):
        if not self.keys.__contains__((str(id), name_student, surname_student)):
            raise Exception("There_is_not_such_student")