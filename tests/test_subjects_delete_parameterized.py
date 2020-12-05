import unittest
from src.subjects import Subjects
from parameterized import parameterized, parameterized_class


class SubjectsDeleteParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Subjects()

    @parameterized.expand([
        (5, "Piotr", "Fantazja", "math", {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}),
    ])
    def test_delete_subjects_positive_expand(self, id, name, surname, name_subject, expected):
        self.assertEqual(self.tmp.deleteSubject(id, name, surname, name_subject), expected)


if __name__ == '__main__':
    unittest.main()
