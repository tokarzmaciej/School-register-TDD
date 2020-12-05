import unittest
from hamcrest import *
from src.remark import Remarks


class RemarksAddHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Remarks()

    def test_add_remark_lack_student(self):
        assert_that(calling(self.temp.addRemark)
                    .with_args(10, "Gosia", "Rosa", "help", "preparing_appeal"),
                    raises(Exception))

    def tearDown(self):
        self.temp = None
