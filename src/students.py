class Students:
    def __init__(self):
        self.students = {
            ("1", "Kasia", "Polak"): {
                "subjects": {

                },
                "remarks": {

                }
            },
            ("2", "Beata", "Jankowska"): {
                "subjects": {

                },
                "remarks": {

                }
            },
            ("3", "Kacper", "Stoch"): {
                "subjects": {

                },
                "remarks": {

                }
            },
            ("4", "Alicja", "Zielonka"): {
                "subjects": {
                    "match": {

                    },
                    "english": {

                    }
                },
                "remarks": {

                }
            },
            ("5", "Piotr", "Fantazja"): {
                "subjects": {
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
                "subjects": {
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
                "subjects": {
                    "physics": {
                        "test_planets": 5,
                        "activity1": 4,
                        "quiz": 2,
                    },
                    "geography": {
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
            ("8", "Konrad", "Piasek"): {
                "subjects": {
                },
                "remarks": {
                    "disturbing_lesson": "talking during classes",
                    "competition": "second place"
                }
            },

        }
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
