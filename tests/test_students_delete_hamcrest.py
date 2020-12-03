import unittest
from hamcrest import *
from src.students import Students


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_delete_lack_student(self):
        assert_that(calling(self.temp.deleteStudent)
                    .with_args(3, "Kasia", "Polak"),
                    raises(Exception))

    def test_delete_student(self):
        assert_that(self.temp.deleteStudent(1, "Kasia", "Polak"),
                    not_(contains_exactly(('1', 'Kasia', 'Polak'))))

    def tearDown(self):
        self.temp = None
