import csv
import json


class Service:
    def __init__(self):
        self.data = self.importStudents()
    def exportStudent(self, id, name, surname, subjects, remarks):
        if self.data == {}:
            with open("./db.csv", "w", newline='') as file:
                data = csv.writer(file, delimiter=",")
                data.writerow(["id", "name", "surname", "subjects", "remarks"])
                data.writerow([id, name, surname, subjects, remarks])
                return True
        else:
            with open("./db.csv", "a", newline='') as file:
                data = csv.writer(file, delimiter=",")
                data.writerow([id, name, surname, subjects, remarks])
                return True

    def importStudents(self):
        with open("./db.csv", "r", newline='') as file:
            data = csv.DictReader(file, delimiter=",")
            students = {}
            for row in data:
                students[(str(row["id"]), str(row["name"]), str(row["surname"]))] = {
                    "subjects": json.loads(row["subjects"]),
                    "remarks": json.loads(row["remarks"])}
            return students
