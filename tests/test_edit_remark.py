import unittest
from assertpy import assert_that
from src.remark import Remarks


class RemarksAddAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Remarks()

    def test_edit_remark_description_positive(self):
        assert_that(self.temp.editRemarkDescription(7, "Ewelina", "Swoboda", "competition", "second_place")) \
            .starts_with("second")

    def test_edit_remark_description_lack_remark(self):
        assert_that(self.temp.editRemarkDescription) \
            .raises(Exception).when_called_with(3, "Kacper", "Stoch", "volunteering", "helping_an_elderly_person")

    def test_edit_remark_description_lack_students(self):
        assert_that(self.temp.editRemarkDescription) \
            .raises(Exception).when_called_with(14, "Julka", "Ostrowska", "competition", "first_place")

    def tearDown(self):
        self.temp = None
