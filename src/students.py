class Students:
    def __init__(self):
        self.students = {
            ("1", "Kasia", "Polak"): {
                "subject": {

                },
                "remarks": {

                }
            },
            ("2", "Beata", "Jankowska"): {
                "subject": {

                },
                "remarks": {

                }
            },
            ("3", "Kacper", "Stoch"): {
                "subject": {

                },
                "remarks": {

                }
            },
            ("4", "Alicja", "Zielonka"): {
                "subject": {
                    "match": {

                    },
                    "english": {

                    }
                },
                "remarks": {

                }
            },
            ("5", "Piotr", "Fantazja"): {
                "subject": {
                    "match": {

                    },
                    "history": {

                    },
                    "art": {

                    }
                },
                "remarks": {

                }
            },
            ("6", "Michal", "Krakowiak"): {
                "subject": {
                    "match": {
                        "activity1": 5,
                        "test_addition": 4,
                        "quiz": 6,
                    },
                    "history": {
                        "exam": 3,
                        "activity1": 4,
                        "activity2": 5,
                    },
                    "art": {
                        "painting_landscape": 3,
                        "test_monuments": 2,
                        "singing_hymn": 6,
                        "activity1": 5,
                    }
                },
                "remarks": {

                }
            },
            ("7", "Ewelina", "Swoboda"): {
                "subject": {
                    "physics": {
                        "test_planets": 5,
                        "activity1": 4,
                        "quiz": 2,
                    },
                    "geogrphy": {
                        "exam": 4,
                        "test_map": 4,
                        "activity1": 5,
                    },
                },
                "remarks": {
                    "volunteering": "helping an elderly person",
                    "competition": "first place"
                }
            },
            ("8", "Kondrad", "Piasek"): {
                "subject": {
                },
                "remarks": {
                    "disturbing_lesson": "talking during classes",
                    "competition": "second place"
                }
            },

        }

    def addStudent(self, id_student, name, surname):
        if type(name) != str or type(surname) != str:
            raise TypeError("Bad_type_name_or_surname")
        else:
            keys = [*self.students]
            for i in range(len(keys)):
                keys[i] = str(keys[i][0])
            if keys.__contains__(str(id_student)):
                raise Exception("This_id_already_exists")
            else:
                self.students[(str(id_student), name, surname)] = {}
                self.students[(str(id_student), name, surname)]["subjects"] = {}
                self.students[(str(id_student), name, surname)]["remarks"] = {}
                return 'Add student', name, surname, self.students[(str(id_student), name, surname)]

    def deleteStudent(self, id_student, name_student, surname_student):
        keys = [*self.students]
        if keys.__contains__((str(id_student), name_student, surname_student)):
            self.students.pop((str(id_student), name_student, surname_student))
            return list(self.students)
        else:
            raise Exception("There_is_not_such_student")

    def editStudent(self, id_student, name_student, surname_student, new_name, new_surname):
        keys = [*self.students]
        if type(new_name) != str or type(new_surname) != str:
            raise TypeError("Bad_type_newName_or_newSurname")
        else:
            if keys.__contains__((str(id_student), name_student, surname_student)):
                self.students[(str(id_student), new_name, new_surname)] = self.students.pop(
                    (str(id_student), name_student, surname_student))
                return list(filter(lambda x: x == (str(id_student), new_name, new_surname), list(self.students)))
            else:
                raise Exception("There_is_not_such_student")
