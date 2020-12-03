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

    @parameterized.expand([
        (2, "Aneta", "Czarna", "Asia", "Pola", "There_is_not_such_student"),
    ])
    def test_student_edit_exceptions_expand(self, id, name, surname, new_name, new_surname, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.editStudent, id, name, surname, new_name, new_surname)

    @parameterized.expand([
        (2, "Marcel", "Bialy", None, "Pola", "Bad_type_newName_or_newSurname")
    ])
    def test_student_edit_type_error_expand(self, id, name, surname, new_name, new_surname, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.editStudent, id, name, surname, new_name, new_surname)


if __name__ == '__main__':
    unittest.main()
