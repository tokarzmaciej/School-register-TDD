import unittest
from key_generator.key_generator import generate
from src.students import Students
from parameterized import parameterized, parameterized_class


class StudentsParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Students()

    @parameterized.expand([
        (generate().get_key(), "Adam", "Nowak", ('Add student', 'Adam', 'Nowak', {'subjects': {}, 'remarks': {}})),
    ])
    def test_student_add_expand(self, id, name, surname, expected):
        self.assertEqual(self.tmp.addStudent(id, name, surname), expected)

    @parameterized.expand([
        (2, "Beata", "Jankowska", "This_id_already_exists"),
    ])
    def test_student_add_exceptions_expand(self, id, name, surname, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.addStudent, id, name, surname)


if __name__ == '__main__':
    unittest.main()
