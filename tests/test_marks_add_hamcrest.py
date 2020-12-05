import unittest
from hamcrest import *
from src.marks import Marks


class MarksAddHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Marks()

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
