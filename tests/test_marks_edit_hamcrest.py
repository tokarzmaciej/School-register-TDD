import unittest
from hamcrest import *
from src.marks import Marks
from src.exampleData import Data


class MarksEditHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Marks(Data().example)

    def test_edit_mark_positive(self):
        assert_that(self.temp.editMark(7, "Ewelina", "Swoboda", "physics", "quiz", 4),
                    has_item(('quiz', 4)))

    def test_edit_mark_lack_mark(self):
        assert_that(calling(self.temp.editMark)
                    .with_args(6, "Michal", "Krakowiak", "math", "exam", 3),
                    raises(Exception))

    def test_edit_mark_lack_subjects(self):
        assert_that(calling(self.temp.editMark)
                    .with_args(4, "Alicja", "Zielonka", "history", "test", 3),
                    raises(Exception))

    def test_edit_mark_lack_student(self):
        assert_that(calling(self.temp.editMark)
                    .with_args(10, "Ewa", "Piech", "english", "quiz", 5),
                    raises(Exception))

    def test_edit_mark_grade_bad_type(self):
        assert_that(calling(self.temp.editMark)
                    .with_args(7, "Ewelina", "Swoboda", "physics", "quiz", False),
                    raises(TypeError))

    def tearDown(self):
        self.temp = None
