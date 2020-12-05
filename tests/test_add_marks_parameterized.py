import unittest
from src.marks import Marks
from parameterized import parameterized, parameterized_class


class MarksAddParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Marks()

    @parameterized.expand([
        (4, "Alicja", "Zielonka", "math", "test", 2, ('test', 2)),
    ])
    def test_delete_subjects_positive_expand(self, id, name, surname, name_subject, name_mark, grade, expected):
        self.assertIn(expected, self.tmp.addMark(id, name, surname, name_subject, name_mark, grade))


if __name__ == '__main__':
    unittest.main()
