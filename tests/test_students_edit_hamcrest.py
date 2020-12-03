import unittest
from hamcrest import *
from src.students import Students


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_edit_student_positive(self):
        assert_that(self.temp.editStudent(1, "Kasia", "Polak", "Asia", "Pola")[0][1],
                    contains_string("Asia"))


    def tearDown(self):
        self.temp = None
