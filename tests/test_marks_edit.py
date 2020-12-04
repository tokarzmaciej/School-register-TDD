import unittest
from assertpy import assert_that
from src.marks import Marks


class MarksEditAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Marks()

    def test_edit_mark_positive(self):
        assert_that(self.temp.editMark(7, "Ewelina", "Swoboda", "physics", "quiz", 4)) \
            .contains(('quiz', 4))

    def test_edit_mark_lack_mark(self):
        assert_that(self.temp.editMark) \
            .raises(Exception).when_called_with(6, "Michal", "Krakowiak", "math", "exam", 3)

    def test_edit_mark_lack_subjects(self):
        assert_that(self.temp.editMark) \
            .raises(Exception).when_called_with(4, "Alicja", "Zielonka", "history", "test", 3)

    def test_edit_mark_lack_student(self):
        assert_that(self.temp.editMark) \
            .raises(Exception).when_called_with(10, "Ewa", "Piech", "english", "quiz", 5)

    def test_edit_mark_grade_bad_type(self):
        assert_that(self.temp.editMark) \
            .raises(TypeError).when_called_with(7, "Ewelina", "Swoboda", "physics", "quiz", False)

    def tearDown(self):
        self.temp = None
