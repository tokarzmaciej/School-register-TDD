import unittest
from src.subjects import Subjects
from parameterized import parameterized, parameterized_class


class SubjectsEditParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Subjects()

    @parameterized.expand([
        (6, "Michal", "Krakowiak", "art", "history_art", "history_art"),
    ])
    def test_edit_subjects_positive_expand(self, id, name, surname, name_subject, new_name_subject, expected):
        self.assertIn(expected, self.tmp.editSubject(id, name, surname, name_subject, new_name_subject))


if __name__ == '__main__':
    unittest.main()
