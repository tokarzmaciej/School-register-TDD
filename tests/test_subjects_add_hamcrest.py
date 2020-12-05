import unittest
from hamcrest import *
from src.subjects import Subjects


class SubjectAddHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Subjects()

    def test_add_subject_to_lack_student(self):
        assert_that(calling(self.temp.addSubject)
                    .with_args(12, "Zosia", "Kucharska", "math"),
                    raises(Exception))

    def test_add_subject_name_subject_bad_type(self):
        assert_that(calling(self.temp.addSubject)
                    .with_args(2, "Beata", "Jankowska", True),
                    raises(TypeError))

    def tearDown(self):
        self.temp = None
