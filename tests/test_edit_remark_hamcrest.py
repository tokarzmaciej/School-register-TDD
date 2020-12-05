import unittest
from hamcrest import *
from src.remark import Remarks


class RemarksEditHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Remarks()

    def test_edit_remark_description_positive(self):
        assert_that(self.temp.editRemarkDescription(7, "Ewelina", "Swoboda", "competition", "second_place"),
                    starts_with("second"))

    def test_edit_remark_description_lack_remark(self):
        assert_that(calling(self.temp.editRemarkDescription)
                    .with_args(3, "Kacper", "Stoch", "volunteering", "helping_an_elderly_person"),
                    raises(Exception))

    def test_edit_remark_description_lack_students(self):
        assert_that(calling(self.temp.editRemarkDescription)
                    .with_args(14, "Julka", "Ostrowska", "competition", "first_place"),
                    raises(Exception))

    def tearDown(self):
        self.temp = None
