class Students:
    def __init__(self):
        self.students = {}

    def addStudent(self, id, name, surname, option):
        if type(name) != str or type(surname) != str:
            raise TypeError("Bad_type_name_or_surname")
        elif option != "w":
            raise Exception("Option_have_to_be_'w'_or_'a'")
        else:
            return ('Add student', 'Adam', 'Nowak', {'subjects': {}, 'remarks': {}})