import unittest
from key_generator.key_generator import generate
from src.subjects import Subjects
from parameterized import parameterized, parameterized_class


class StudentsParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Subjects()

    @parameterized.expand([
        (2, "Beata", "Jankowska", "english", {'subjects': {"english": {}}, 'remarks': {}}),
    ])
    def test_add_subjects_positive_expand(self, id, name, surname, name_subject, expected):
        self.assertEqual(self.tmp.addSubject(id, name, surname, name_subject), expected)


if __name__ == '__main__':
    unittest.main()
