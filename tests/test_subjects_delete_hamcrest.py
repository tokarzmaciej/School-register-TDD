import unittest
from hamcrest import *
from src.subjects import Subjects


class StudentsHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Subjects()

    def test_delete_subject_to_lack_subject(self):
        assert_that(calling(self.temp.deleteSubject)
                    .with_args(5, "Piotr", "Fantazja", "geography"),
                    raises(Exception))

    def test_delete_subject_to_lack_student(self):
        assert_that(calling(self.temp.deleteSubject)
                    .with_args(10, "Ania", "Zegan", "english"),
                    raises(Exception))

    def test_delete_subject_name_bad_typ(self):
        assert_that(calling(self.temp.deleteSubject)
                    .with_args(5, "Piotr", "Fantazja", 1234),
                    raises(TypeError))

    def tearDown(self):
        self.temp = None
