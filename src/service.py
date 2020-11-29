import csv
import json


def export_student(id, name, surname, subjects, remarks):
    if import_students() == {}:
        with open("./data/db.csv", "a", newline='') as file:
            data = csv.writer(file, delimiter=",")
            data.writerow(["id", "name", "surname", "subjects", "remarks"])
            data.writerow([id, name, surname, subjects, remarks])
    else:
        with open("./data/db.csv", "a", newline='') as file:
            data = csv.writer(file, delimiter=",")
            data.writerow([id, name, surname, subjects, remarks])


def import_students():
    with open("./data/db.csv", "r", newline='') as file:
        data = csv.DictReader(file, delimiter=",")
        students = {}
        for row in data:
            students[(str(row["id"]), str(row["name"]), str(row["surname"]))] = {
                "subjects": json.loads(row["subjects"]),
                "remarks": json.loads(row["remarks"])}
        return students


def reset():
    reset = open("./data/db.csv", "w")
    reset.write("")
    reset.close()
