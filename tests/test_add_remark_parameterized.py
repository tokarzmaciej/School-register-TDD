import unittest
from src.remark import Remarks
from parameterized import parameterized, parameterized_class


class RemarksAddParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Remarks()

    @parameterized.expand([
        (2, "Beata", "Jankowska", "volunteering", "cleaning_the_environment",
         {'volunteering': 'cleaning_the_environment'}),
    ])
    def test_add_remark_positive_expand(self, id, name, surname, name_remark, description_remark, expected):
        self.assertEqual(expected, self.tmp.addRemark(id, name, surname, name_remark, description_remark))


if __name__ == '__main__':
    unittest.main()
