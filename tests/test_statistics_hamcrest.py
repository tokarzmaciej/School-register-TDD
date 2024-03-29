import unittest
from hamcrest import *
from src.statistics import Statistics
from src.exampleData import Data


class AverageHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Statistics(Data().example)

    def test_average_subjects_positive(self):
        assert_that(
            self.temp.averageSubjects(7, "Ewelina", "Swoboda")[1],
            less_than_or_equal_to(4))

    def test_average_subjects_lack_marks(self):
        assert_that(calling(self.temp.averageSubjects)
                    .with_args(4, "Alicja", "Zielonka"),
                    raises(Exception))

    def test_average_subjects_lack_subjects(self):
        assert_that(calling(self.temp.averageSubjects)
                    .with_args(3, "Kacper", "Stoch"),
                    raises(Exception))

    def test_average_subjects_lack_student(self):
        assert_that(calling(self.temp.averageSubjects)
                    .with_args(21, "Piotr", "Lewandowski"),
                    raises(Exception))

    def test_average_subject_positive(self):
        assert_that(
            self.temp.averageSubject(6, "Michal", "Krakowiak", "math")[1],
            greater_than_or_equal_to(5))

    def test_average_subject_lack_marks(self):
        assert_that(calling(self.temp.averageSubject)
                    .with_args(5, "Piotr", "Fantazja", "art"),
                    raises(Exception))

    def test_average_subject_lack_subject(self):
        assert_that(calling(self.temp.averageSubject)
                    .with_args(4, "Alicja", "Zielonka", "history"),
                    raises(Exception))

    def test_average_subject_lack_student(self):
        assert_that(calling(self.temp.averageSubject)
                    .with_args(21, "Zosia", "Borkowska", "math"),
                    raises(Exception))

    def tearDown(self):
        self.temp = None
