import unittest
from src.remark import Remarks
from parameterized import parameterized, parameterized_class


class RemarksEditParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Remarks()

    @parameterized.expand([
        (8, "Konrad", "Piasek", "disturbing_lesson", "disturbing_math_lesson", "math_lesson")
    ])
    def test_edit_remark_name_expand(self, id, name, surname, name_remark, new_name_remark, expected):
        self.assertIn(expected, self.tmp.editRemarkName(id, name, surname, name_remark, new_name_remark)[1])

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", "competition", "second_place", "second")
    ])
    def test_edit_remark_description_expand(self, id, name, surname, name_remark, new_description_remark, expected):
        self.assertIn(expected, self.tmp.editRemarkDescription(id, name, surname, name_remark, new_description_remark))


if __name__ == '__main__':
    unittest.main()
