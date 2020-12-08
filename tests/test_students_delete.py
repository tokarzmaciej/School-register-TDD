import unittest
from assertpy import assert_that
from src.students import Students
from src.exampleData import Data


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students(Data().example)

    def test_delete_lack_student(self):
        assert_that(self.temp.deleteStudent) \
            .raises(Exception) \
            .when_called_with(3, "Kasia", "Polak")

    def test_delete_student(self):
        assert_that(self.temp.deleteStudent(1, "Kasia", "Polak")) \
            .does_not_contain(('1', 'Kasia', 'Polak'))

    def tearDown(self):
        self.temp = None
