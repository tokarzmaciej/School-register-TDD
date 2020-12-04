from src.students import *


class Remarks(Students):

    def addRemark(self, id, name_student, surname_student, name_remark, description_remark):
        if not self.keys.__contains__((str(id), name_student, surname_student)):
            raise Exception("There_is_not_such_student")
