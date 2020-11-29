from src.service import *


class Students:

    def addStudent(self, id, name, surname, option):
        if type(name) != str or type(surname) != str:
            raise TypeError("Bad_type_name_or_surname")
        elif option == "w":
            reset()
            export_student(str(id), name, surname, {}, {})
            return "Add student", name, surname, import_students()[(str(id), name, surname)]
        elif option == "a":
            keys = [*import_students()]
            for i in range(len(keys)):
                keys[i] = keys[i][0]
            if keys.__contains__(str(id)):
                raise Exception("This_id_already_exists")
            else:
                export_student(str(id), name, surname, {}, {})
                return list(import_students())
        else:
            raise Exception("Option_have_to_be_'w'_or_'a'")
    def deleteStudent(self, id, name_student, surname_student):
        keys = [*import_students()]
        students = import_students()
        reset()
        if keys.__contains__((str(id), name_student, surname_student)):
            filterKeys = list(filter(lambda x: x != (str(id), name_student, surname_student), keys))
            for key in filterKeys:
                id = key[0]
                name = key[1]
                surname = key[2]
                subjects = students[key]["subjects"]
                remarks = students[key]["remarks"]
                export_student(id, name, surname, subjects, remarks)
            return list(import_students())
        else:
            raise Exception("There_is_not_such_student")
