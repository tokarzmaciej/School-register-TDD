import unittest
from hamcrest import *
from src.marks import Marks
from src.exampleData import Data


class MarksAddHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Marks(Data().example)

    def test_add_mark_positive(self):
        assert_that(self.temp.addMark(4, "Alicja", "Zielonka", "math", "test", 2),
                    contains_exactly(('test', 2)))

    def test_add_mark_mark_already_exists(self):
        assert_that(calling(self.temp.addMark)
                    .with_args(6, "Michal", "Krakowiak", "art", "singing_hymn", 3),
                    raises(Exception))

    def test_add_mark_lack_subjects(self):
        assert_that(calling(self.temp.addMark)
                    .with_args(3, "Kacper", "Stoch", "geography", "activity", 5),
                    raises(Exception))

    def test_add_mark_lack_student(self):
        assert_that(calling(self.temp.addMark)
                    .with_args(11, "Robert", "Perkoz", "english", "test-present-simple", 3),
                    raises(Exception))

    def test_add_mark_range_mark(self):
        assert_that(calling(self.temp.addMark)
                    .with_args(4, "Alicja", "Zielonka", "math", "test", 7),
                    raises(Exception))

    def test_add_mark_name_bad_type(self):
        assert_that(calling(self.temp.addMark)
                    .with_args(5, "Piotr", "Fantazja", "math", "test", "1"),
                    raises(TypeError))

    def tearDown(self):
        self.temp = None
