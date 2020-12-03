import unittest
from assertpy import assert_that
from src.students import Students


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_edit_student_positive(self):
        assert_that(self.temp.editStudent(1, "Kasia", "Polak", "Asia", "Pola")[0][1]) \
            .contains('Asia')

    def test_edit_lack_student(self):
        assert_that(self.temp.editStudent) \
            .raises(Exception) \
            .when_called_with(2, "Aneta", "Czarna", "Asia", "Pola")

    def test_edit_type_error(self):
        assert_that(self.temp.editStudent) \
            .raises(TypeError) \
            .when_called_with(2, "Marcel", "Bialy", None, "Pola")

    def tearDown(self):
        self.temp = None
