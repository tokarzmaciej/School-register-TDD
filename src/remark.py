from src.students import *


class Remarks(Students):

    def addRemark(self, id, name_student, surname_student, name_remark, description_remark):
        if self.keys.__contains__((str(id), name_student, surname_student)):
            valueRemarks = self.students[(str(id), name_student, surname_student)]["remarks"]
            if [*valueRemarks].__contains__(name_remark):
                raise Exception("This_remark_already_exists")
        else:
            raise Exception("There_is_not_such_student")
