import unittest
from hamcrest import *
from src.subjects import Subjects
from src.exampleData import Data


class SubjectsDeleteHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Subjects(Data().example)

    def test_delete_subject_positive(self):
        result = {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}
        assert_that(self.temp.deleteSubject(5, "Piotr", "Fantazja", "math"), equal_to(result))

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
