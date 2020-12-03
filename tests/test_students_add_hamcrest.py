import unittest
from hamcrest import *
from src.students import Students
from key_generator.key_generator import generate


class StudentsHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_add_student_positive(self):
        result = ('Add student', 'Adam', 'Nowak', {'subjects': {}, 'remarks': {}})
        assert_that(self.temp.addStudent(generate().get_key(), "Adam", "Nowak"), equal_to(result))

    def tearDown(self):
        self.temp = None
