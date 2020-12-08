import unittest
from assertpy import assert_that
from src.remark import Remarks
from src.exampleData import Data


class RemarksAddAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Remarks(Data().example)

    def test_add_remark_positive(self):
        result = {'volunteering': 'cleaning_the_environment'}
        assert_that(self.temp.addRemark(2, "Beata", "Jankowska", "volunteering", "cleaning_the_environment")) \
            .is_equal_to(result)

    def test_add_remark_already_exists(self):
        assert_that(self.temp.addRemark) \
            .raises(Exception).when_called_with(8, "Konrad", "Piasek", "competition", "first place")

    def test_add_remark_lack_student(self):
        assert_that(self.temp.addRemark) \
            .raises(Exception).when_called_with(10, "Gosia", "Rosa", "help", "preparing_appeal")

    def tearDown(self):
        self.temp = None
