import unittest
from assertpy import assert_that
from src.remark import Remarks


class RemarksEditAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Remarks()

    def test_edit_remark_name_positive(self):
        assert_that(self.temp.editRemarkName(8, "Konrad", "Piasek", "disturbing_lesson", "disturbing_math_lesson")[1]) \
            .ends_with("math_lesson")

    def test_edit_remark_name_lack_students(self):
        assert_that(self.temp.editRemarkName) \
            .raises(Exception).when_called_with(15, "Wiktor", "Nowak", "competition", "football_competition")

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
