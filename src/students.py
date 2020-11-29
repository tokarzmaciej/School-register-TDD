import csv
import json


class Students:
    def __init__(self):
        self.students = {}

    def addStudent(self, id, name, surname, option):
        if type(name) != str or type(surname) != str:
            raise TypeError("Bad_type_name_or_surname")
        elif option == "w":
            self.reset()
            self.export_student(str(id), name, surname, {}, {})
            return "Add student", name, surname, self.import_students()[(str(id), name, surname)]
        else:
            raise Exception("Option_have_to_be_'w'_or_'a'")

    def export_student(self, id, name, surname, subjects, remarks):
        with open("./data/db.csv", "a", newline='') as file:
            data = csv.writer(file, delimiter=",")
            data.writerow(["id", "name", "surname", "subjects", "remarks"])
            data.writerow([id, name, surname, subjects, remarks])

    def import_students(self):
        with open("./data/db.csv", "r", newline='') as file:
            data = csv.DictReader(file, delimiter=",")
            students = {}
            for row in data:
                students[(str(row["id"]), str(row["name"]), str(row["surname"]))] = {
                    "subjects": json.loads(row["subjects"]),
                    "remarks": json.loads(row["remarks"])}
            return students

    def reset(self):
        reset = open("./data/db.csv", "w")
        reset.write("")
        reset.close()
