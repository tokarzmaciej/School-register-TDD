import unittest
from hamcrest import *
from src.subjects import Subjects
from src.exampleData import Data


class SubjectsEditHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Subjects(Data().example)

    def test_edit_subject_positive(self):
        assert_that(self.temp.editSubject(6, "Michal", "Krakowiak", "art", "history_art"),
                    has_item('history_art'))

    def test_edit_subject_to_lack_subjects(self):
        assert_that(calling(self.temp.editSubject)
                    .with_args(4, "Alicja", "Zielonka", "history", "world-history"),
                    raises(Exception))

    def test_edit_subject_to_lack_student(self):
        assert_that(calling(self.temp.editSubject)
                    .with_args(2, "Grzegorz", "Kowalczyk", "english", "primary_english"),
                    raises(Exception))

    def test_edit_subject_name_bad_type(self):
        assert_that(calling(self.temp.editSubject)
                    .with_args(5, "Piotr", "Fantazja", "history", False),
                    raises(TypeError))

    def tearDown(self):
        self.temp = None
