import unittest
from assertpy import assert_that
from src.statistics import Statistics


class StatisticsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Statistics()

    def test_average_subjects_lack_marks(self):
        assert_that(self.temp.averageSubjects) \
            .raises(Exception).when_called_with(4, "Alicja", "Zielonka")

    def test_average_subjects_lack_subjects(self):
        assert_that(self.temp.averageSubjects) \
            .raises(Exception).when_called_with(3, "Kacper", "Stoch")

    def test_average_subjects_lack_student(self):
        assert_that(self.temp.averageSubjects) \
            .raises(Exception).when_called_with(21, "Piotr", "Lewandowski")

    def test_average_subject_positive(self):
        assert_that(self.temp.averageSubject(6, "Michal", "Krakowiak", "math")[1]) \
            .is_greater_than_or_equal_to(5)

    def test_average_subject_lack_marks(self):
        assert_that(self.temp.averageSubject) \
            .raises(Exception).when_called_with(5, "Piotr", "Fantazja", "art")

    def test_average_subject_lack_subject(self):
        assert_that(self.temp.averageSubject) \
            .raises(Exception).when_called_with(4, "Alicja", "Zielonka", "history")

    def test_average_subject_lack_student(self):
        assert_that(self.temp.averageSubject) \
            .raises(Exception).when_called_with(21, "Zosia", "Borkowska", "math")

    def tearDown(self):
        self.temp = None
