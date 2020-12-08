import unittest
from hamcrest import *
from src.remark import Remarks
from src.exampleData import Data


class RemarksAddHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Remarks(Data().example)

    def test_add_remark_positive(self):
        result = {'volunteering': 'cleaning_the_environment'}
        assert_that(self.temp.addRemark(2, "Beata", "Jankowska", "volunteering", "cleaning_the_environment"),
                    equal_to(result))

    def test_add_remark_already_exists(self):
        assert_that(calling(self.temp.addRemark)
                    .with_args(8, "Konrad", "Piasek", "competition", "first place"),
                    raises(Exception))

    def test_add_remark_lack_student(self):
        assert_that(calling(self.temp.addRemark)
                    .with_args(10, "Gosia", "Rosa", "help", "preparing_appeal"),
                    raises(Exception))

    def tearDown(self):
        self.temp = None
