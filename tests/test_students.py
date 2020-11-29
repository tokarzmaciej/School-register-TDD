import unittest
from assertpy import assert_that
from src.students import Students


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()
    def test_add_student_surname_bad_type(self):
        assert_that(self.temp.addStudent) \
            .raises(TypeError) \
            .when_called_with(2, "Jan", 2, "w")
    def test_add_student_name_bad_type(self):
        assert_that(self.temp.addStudent) \
            .raises(TypeError).when_called_with(2, True, "Kowalski", "w")

    def tearDown(self):
        self.temp = None
