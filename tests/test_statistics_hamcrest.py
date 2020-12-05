import unittest
from hamcrest import *
from src.statistics import Statistics


class AverageHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Statistics()

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
