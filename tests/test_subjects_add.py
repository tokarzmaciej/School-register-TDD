import unittest
from assertpy import assert_that
from src.subjects import Subjects


class SubjectsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Subjects()

    def test_add_subject_name_subject_bad_type(self):
        assert_that(self.temp.addSubject) \
            .raises(TypeError).when_called_with(2, "Beata", "Jankowska", True)

    def tearDown(self):
        self.temp = None
