import unittest
from assertpy import assert_that
from src.marks import Marks
from src.exampleData import Data


class MarksAddAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Marks(Data().example)

    def test_add_mark_positive(self):
        assert_that(self.temp.addMark(4, "Alicja", "Zielonka", "math", "test", 2)) \
            .contains(('test', 2))

    def test_add_mark_mark_already_exists(self):
        assert_that(self.temp.addMark) \
            .raises(Exception).when_called_with(6, "Michal", "Krakowiak", "art", "singing_hymn", 3)

    def test_add_mark_lack_subjects(self):
        assert_that(self.temp.addMark) \
            .raises(Exception).when_called_with(3, "Kacper", "Stoch", "geography", "activity", 5)

    def test_add_mark_lack_student(self):
        assert_that(self.temp.addMark) \
            .raises(Exception).when_called_with(11, "Robert", "Perkoz", "english", "test-present-simple", 3)

    def test_add_mark_range_mark(self):
        assert_that(self.temp.addMark) \
            .raises(Exception).when_called_with(4, "Alicja", "Zielonka", "math", "test", 7)

    def test_add_mark_name_bad_type(self):
        assert_that(self.temp.addMark) \
            .raises(TypeError).when_called_with(5, "Piotr", "Fantazja", "math", "test", "1")

    def tearDown(self):
        self.temp = None
