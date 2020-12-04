import unittest
from assertpy import assert_that
from src.statistics import Statistics


class StatisticsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Statistics()

    def test_average_subject_lack_student(self):
        assert_that(self.temp.averageSubject) \
            .raises(Exception).when_called_with(21, "Zosia", "Borkowska", "math")

    def tearDown(self):
        self.temp = None
