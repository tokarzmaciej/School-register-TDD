import unittest
from src.students import Students
from parameterized import parameterized, parameterized_class


class StudentsParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Students()

    @parameterized.expand([
        (1, "Kasia", "Polak", ('1', 'Kasia', 'Polak')),
    ])
    def test_student_delete_expand(self, id, name, surname, expected):
        self.assertNotIn(self.tmp.deleteStudent(id, name, surname), expected)


if __name__ == '__main__':
    unittest.main()
