import unittest
from hamcrest import *
from src.marks import Marks


class MarksEditHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Marks()

    def test_edit_mark_grade_bad_type(self):
        assert_that(calling(self.temp.editMark)
                    .with_args(7, "Ewelina", "Swoboda", "physics", "quiz", False),
                    raises(TypeError))

    def tearDown(self):
        self.temp = None
