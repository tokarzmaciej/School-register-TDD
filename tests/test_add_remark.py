import unittest
from assertpy import assert_that
from src.remark import Remarks


class RemarksAddAssertPyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Remarks()

    def test_add_remark_lack_student(self):
        assert_that(self.temp.addRemark) \
            .raises(Exception).when_called_with(10, "Gosia", "Rosa", "help", "preparing_appeal")

    def tearDown(self):
        self.temp = None
