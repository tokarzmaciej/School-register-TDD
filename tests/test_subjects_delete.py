import unittest
from assertpy import assert_that
from src.subjects import Subjects


class SubjectsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Subjects()

    def test_delete_subject_to_lack_student(self):
        assert_that(self.temp.deleteSubject) \
            .raises(Exception).when_called_with(10, "Ania", "Zegan", "english")

    def tearDown(self):
        self.temp = None