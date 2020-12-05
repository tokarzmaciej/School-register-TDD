import unittest
from src.marks import Marks
from parameterized import parameterized, parameterized_class


class MarksEditParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Marks()

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", "physics", "quiz", 4, ('quiz', 4)),
    ])
    def test_edit_mark_positive_expand(self, id, name, surname, name_subject, name_mark, grade, expected):
        self.assertIn(expected, self.tmp.editMark(id, name, surname, name_subject, name_mark, grade))


if __name__ == '__main__':
    unittest.main()
