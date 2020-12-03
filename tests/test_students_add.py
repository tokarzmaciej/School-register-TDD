import unittest
from assertpy import assert_that
from src.students import Students
from key_generator.key_generator import generate


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_add_student_positive(self):
        result = ('Add student', 'Adam', 'Nowak', {'subjects': {}, 'remarks': {}})
        assert_that(self.temp.addStudent(generate().get_key(), "Adam", "Nowak")) \
            .is_equal_to(result)

    def test_add_the_same_students(self):
        assert_that(self.temp.addStudent) \
            .raises(Exception) \
            .when_called_with(2, "Beata", "Jankowska")

    def test_add_student_surname_bad_type(self):
        assert_that(self.temp.addStudent) \
            .raises(TypeError) \
            .when_called_with(generate().get_key(), "Jan", 2)

    def test_add_student_name_bad_type(self):
        assert_that(self.temp.addStudent) \
            .raises(TypeError) \
            .when_called_with(generate().get_key(), True, "Kowalski")

    def tearDown(self):
        self.temp = None
