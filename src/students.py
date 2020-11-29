from src.service import *


class Students:

    def addStudent(self, id_student, name, surname, option):
        if type(name) != str or type(surname) != str:
            raise TypeError("Bad_type_name_or_surname")
        elif option == "w":
            reset()
            exportStudent(str(id_student), name, surname, {}, {})
            return "Add student", name, surname, importStudents()[(str(id_student), name, surname)]
        elif option == "a":
            keys = [*importStudents()]
            for i in range(len(keys)):
                keys[i] = keys[i][0]
            if keys.__contains__(str(id_student)):
                raise Exception("This_id_already_exists")
            else:
                exportStudent(str(id_student), name, surname, {}, {})
                return list(importStudents())
        else:
            raise Exception("Option_have_to_be_'w'_or_'a'")

    def deleteStudent(self, id_student, name_student, surname_student):
        keys = [*importStudents()]
        students = importStudents()
        reset()
        if keys.__contains__((str(id_student), name_student, surname_student)):
            filterKeys = list(filter(lambda x: x != (str(id_student), name_student, surname_student), keys))
            for key in filterKeys:
                id_student = key[0]
                name = key[1]
                surname = key[2]
                subjects = students[key]["subjects"]
                remarks = students[key]["remarks"]
                exportStudent(id_student, name, surname, subjects, remarks)
            return list(importStudents())
        else:
            raise Exception("There_is_not_such_student")

    def editStudent(self, id_student, name_student, surname_student, new_name, new_surname):
        keys = [*importStudents()]
        students = importStudents()
        reset()
        if type(new_name) != str or type(new_surname) != str:
            raise TypeError("Bad_type_newName_or_newSurname")
        elif not keys.__contains__((str(id_student), name_student, surname_student)):
            raise Exception("There_is_not_such_student")
        else:
            for key in keys:
                subjects = students[key]["subjects"]
                remarks = students[key]["remarks"]
                if key == (str(id_student), name_student, surname_student):
                    exportStudent(id_student, new_name, new_surname, subjects, remarks)
                else:
                    exportStudent(key[0], key[1], key[2], subjects, remarks)
            return list(filter(lambda x: x == (str(id_student), new_name, new_surname), list(importStudents())))

