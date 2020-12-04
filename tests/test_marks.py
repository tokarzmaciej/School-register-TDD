import unittest
from assertpy import assert_that
from src.marks import Marks


class SubjectsAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Marks()

    def test_add_mark_name_bad_type(self):
        assert_that(self.temp.addMark) \
            .raises(TypeError).when_called_with(5, "Piotr", "Fantazja", "math", "test", "1")

    def tearDown(self):
        self.temp = None
