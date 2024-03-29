import unittest
from src.statistics import Statistics
from parameterized import parameterized, parameterized_class
from src.exampleData import Data


class StatisticsParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Statistics(Data().example)

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", 4)
    ])
    def test_average_subjects_expand(self, id_student, name, surname, expected):
        self.assertLessEqual(expected, self.tmp.averageSubjects(id_student, name, surname)[1])

    @parameterized.expand([
        (6, "Michal", "Krakowiak", "math", 5)
    ])
    def test_average_subject_expand(self, id_student, name, surname, name_subject, expected):
        self.assertGreaterEqual(expected, self.tmp.averageSubject(id_student, name, surname, name_subject)[1])

    @parameterized.expand([
        (4, "Alicja", "Zielonka", "Do_not_have_marks"),
        (3, "Kacper", "Stoch", "Do_not_have_subjects"),
        (21, "Piotr", "Lewandowski", "There_is_not_such_student")
    ])
    def test_average_subjects_exceptions_expand(self, id_student, name, surname, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.averageSubjects, id_student, name, surname)

    @parameterized.expand([
        (5, "Piotr", "Fantazja", "art", "Do_not_have_marks"),
        (4, "Alicja", "Zielonka", "history", "Student_not_have_this_subject"),
        (21, "Zosia", "Borkowska", "math", "There_is_not_such_student")
    ])
    def test_average_subject_exceptions_expand(self, id_student, name, surname, name_subject, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.averageSubject, id_student, name, surname, name_subject)

    @parameterized_class(("id", "name", "surname", "expected"), [
        (7, "Ewelina", "Swoboda", 4)
    ])
    class StatisticsSubjectsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Statistics(Data().example)

        def test_average_subjects_class(self):
            self.assertLessEqual(self.expected, self.tmp.averageSubjects(self.id, self.name, self.surname)[1])

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (6, "Michal", "Krakowiak", "math", 5)
    ])
    class StatisticsSubjectParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Statistics(Data().example)

        def test_average_subject_class(self):
            self.assertGreaterEqual(self.expected,
                                    self.tmp.averageSubject(self.id, self.name, self.surname, self.name_subject)[1])

    @parameterized_class(("id", "name", "surname", "expected"), [
        (4, "Alicja", "Zielonka", "Do_not_have_marks"),
        (3, "Kacper", "Stoch", "Do_not_have_subjects"),
        (21, "Piotr", "Lewandowski", "There_is_not_such_student")
    ])
    class StatisticsSubjectsExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Statistics(Data().example)

        def test_average_subjects_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.averageSubjects, self.id, self.name, self.surname)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (5, "Piotr", "Fantazja", "art", "Do_not_have_marks"),
        (4, "Alicja", "Zielonka", "history", "Student_not_have_this_subject"),
        (21, "Zosia", "Borkowska", "math", "There_is_not_such_student")
    ])
    class StatisticsSubjectExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Statistics(Data().example)

        def test_average_subject_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.averageSubject, self.id, self.name, self.surname,
                                   self.name_subject)


if __name__ == '__main__':
    unittest.main()
