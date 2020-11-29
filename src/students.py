class Students:
    def __init__(self):
        self.students = {}

    def addStudent(self, id, name, surname, option):
        if type(name) != str:
            raise TypeError("Bad_type_name_or_surname")
