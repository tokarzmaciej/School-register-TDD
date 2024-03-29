from src.students import *


class Remarks(Students):

    def addRemark(self, id_student, name_student, surname_student, name_remark, description_remark):
        if self.keys.__contains__((str(id_student), name_student, surname_student)):
            valueRemarks = self.students[(str(id_student), name_student, surname_student)]["remarks"]
            if [*valueRemarks].__contains__(name_remark):
                raise Exception("This_remark_already_exists")
            else:
                valueRemarks[name_remark] = description_remark
                return self.students[(str(id_student), name_student, surname_student)]["remarks"]
        else:
            raise Exception("There_is_not_such_student")

    def editRemarkDescription(self, id_student, name_student, surname_student, name_remark, new_description_remark):
        if self.keys.__contains__((str(id_student), name_student, surname_student)):
            valueRemarks = self.students[(str(id_student), name_student, surname_student)]["remarks"]
            if [*valueRemarks].__contains__(
                    name_remark):
                valueRemarks[name_remark] = new_description_remark
                return valueRemarks[name_remark]
            else:
                raise Exception("Student_not_have_this_remark")
        else:
            raise Exception("There_is_not_such_student")

    def editRemarkName(self, id_student, name_student, surname_student, name_remark, new_name_remark):
        if self.keys.__contains__((str(id_student), name_student, surname_student)):
            valueRemarks = self.students[(str(id_student), name_student, surname_student)]["remarks"]
            if [*valueRemarks].__contains__(name_remark):
                valueRemarks[new_name_remark] = valueRemarks.pop(name_remark)
                return [*valueRemarks]
            else:
                raise Exception("Student_not_have_this_remark")
        else:
            raise Exception("There_is_not_such_student")
