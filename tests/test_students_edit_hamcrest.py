import unittest
from hamcrest import *
from src.students import Students


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_edit_student_positive(self):
        assert_that(self.temp.editStudent(1, "Kasia", "Polak", "Asia", "Pola")[0][1],
                    contains_string("Asia"))

    def test_edit_lack_student(self):
        assert_that(calling(self.temp.editStudent)
                    .with_args(2, "Aneta", "Czarna", "Asia", "Pola"),
                    raises(Exception))

    def test_edit_type_error(self):
        assert_that(calling(self.temp.editStudent)
                    .with_args(2, "Marcel", "Bialy", None, "Pola"),
                    raises(Exception))

    def tearDown(self):
        self.temp = None
