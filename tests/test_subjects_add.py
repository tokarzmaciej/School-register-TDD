import unittest
from assertpy import assert_that
from src.subjects import Subjects
from src.exampleData import Data


class SubjectsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Subjects(Data().example)

    def test_add_subjects_positive(self):
        result = {'subjects': {"english": {}}, 'remarks': {}}
        assert_that(self.temp.addSubject(2, "Beata", "Jankowska", "english")) \
            .is_equal_to(result)

    def test_add_subject_to_lack_student(self):
        assert_that(self.temp.addSubject) \
            .raises(Exception).when_called_with(12, "Zosia", "Kucharska", "math")

    def test_add_subject_name_subject_bad_type(self):
        assert_that(self.temp.addSubject) \
            .raises(TypeError).when_called_with(2, "Beata", "Jankowska", True)

    def tearDown(self):
        self.temp = None
