class Students:
    def __init__(self,dane):
        self.students = dane
        self.keys = [*self.students]

    def addStudent(self, id_student, name, surname):
        if type(name) != str or type(surname) != str:
            raise TypeError("Bad_type_name_or_surname")
        else:
            for i in range(len(self.keys)):
                self.keys[i] = str(self.keys[i][0])
            if self.keys.__contains__(str(id_student)):
                raise Exception("This_id_already_exists")
            else:
                self.students[(str(id_student), name, surname)] = {}
                self.students[(str(id_student), name, surname)]["subjects"] = {}
                self.students[(str(id_student), name, surname)]["remarks"] = {}
                return 'Add student', name, surname, self.students[(str(id_student), name, surname)]

    def deleteStudent(self, id_student, name_student, surname_student):
        if self.keys.__contains__((str(id_student), name_student, surname_student)):
            self.students.pop((str(id_student), name_student, surname_student))
            return list(self.students)
        else:
            raise Exception("There_is_not_such_student")

    def editStudent(self, id_student, name_student, surname_student, new_name, new_surname):
        if type(new_name) != str or type(new_surname) != str:
            raise TypeError("Bad_type_newName_or_newSurname")
        else:
            if self.keys.__contains__((str(id_student), name_student, surname_student)):
                self.students[(str(id_student), new_name, new_surname)] = self.students.pop(
                    (str(id_student), name_student, surname_student))
                return list(filter(lambda x: x == (str(id_student), new_name, new_surname), list(self.students)))
            else:
                raise Exception("There_is_not_such_student")
