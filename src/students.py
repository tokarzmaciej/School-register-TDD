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
            export_student(str(id), name, surname, {}, {})
            return list(import_students())
        else:
            raise Exception("Option_have_to_be_'w'_or_'a'")

