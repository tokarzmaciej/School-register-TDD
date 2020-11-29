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
