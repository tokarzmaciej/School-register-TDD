import unittest
from src.students import Students
from parameterized import parameterized, parameterized_class


class StudentsParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Students()

    @parameterized.expand([
        (1, "Kasia", "Polak", "Asia", "Pola", "Asia"),
    ])
    def test_student_edit_expand(self, id, name, surname, new_name, new_surname, expected):
        self.assertIn(self.tmp.editStudent(id, name, surname, new_name, new_surname)[0][1], expected)



if __name__ == '__main__':
    unittest.main()
