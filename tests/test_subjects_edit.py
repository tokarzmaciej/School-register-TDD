import unittest
from assertpy import assert_that
from src.subjects import Subjects


class SubjectsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Subjects()

    def test_edit_subject_to_lack_student(self):
        assert_that(self.temp.editSubject) \
            .raises(Exception).when_called_with(2, "Grzegorz", "Kowalczyk", "english", "primary_english")

    def test_edit_subject_name_bad_type(self):
        assert_that(self.temp.editSubject) \
            .raises(TypeError).when_called_with(5, "Piotr", "Fantazja", "history", False)

    def tearDown(self):
        self.temp = None
