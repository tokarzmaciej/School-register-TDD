import unittest
from assertpy import assert_that
from src.subjects import Subjects
from src.exampleData import Data


class SubjectsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Subjects(Data().example)

    def test_delete_subject_positive(self):
        result = {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}
        assert_that(self.temp.deleteSubject(5, "Piotr", "Fantazja", "math")) \
            .is_equal_to(result)

    def test_delete_subject_to_lack_subjects(self):
        assert_that(self.temp.deleteSubject) \
            .raises(Exception).when_called_with(5, "Piotr", "Fantazja", "geography")

    def test_delete_subject_name_bad_type(self):
        assert_that(self.temp.deleteSubject) \
            .raises(TypeError).when_called_with(5, "Piotr", "Fantazja", 1234)

    def test_delete_subject_to_lack_student(self):
        assert_that(self.temp.deleteSubject) \
            .raises(Exception).when_called_with(10, "Ania", "Zegan", "english")

    def tearDown(self):
        self.temp = None
