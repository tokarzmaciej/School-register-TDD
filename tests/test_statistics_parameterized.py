import unittest
from src.statistics import Statistics
from parameterized import parameterized, parameterized_class


class StatisticsParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Statistics()

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", 4)
    ])
    def test_average_subjects_expand(self, id, name, surname, expected):
        self.assertLessEqual(expected, self.tmp.averageSubjects(id, name, surname)[1])

    @parameterized.expand([
        (6, "Michal", "Krakowiak", "math", 5)
    ])
    def test_average_subject_expand(self, id, name, surname, name_subject, expected):
        self.assertGreaterEqual(expected, self.tmp.averageSubject(id, name, surname, name_subject)[1])


if __name__ == '__main__':
    unittest.main()
