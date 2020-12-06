import unittest
from src.students import Students
from parameterized import parameterized, parameterized_class


class StudentsParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Students()

    @parameterized.expand([
        (1, "Kasia", "Polak", "Asia", "Pola", "Asia"),
    ])
    def test_student_edit_expand(self, id_student, name, surname, new_name, new_surname, expected):
        self.assertIn(self.tmp.editStudent(id_student, name, surname, new_name, new_surname)[0][1], expected)

    @parameterized.expand([
        (2, "Aneta", "Czarna", "Asia", "Pola", "There_is_not_such_student"),
    ])
    def test_student_edit_exceptions_expand(self, id_student, name, surname, new_name, new_surname, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.editStudent, id_student, name, surname, new_name,
                               new_surname)

    @parameterized.expand([
        (2, "Marcel", "Bialy", None, "Pola", "Bad_type_newName_or_newSurname")
    ])
    def test_student_edit_type_error_expand(self, id_student, name, surname, new_name, new_surname, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.editStudent, id_student, name, surname, new_name,
                               new_surname)

    @parameterized_class(("id", "name", "surname", "new_name", "new_surname", "expected"), [
        (1, "Kasia", "Polak", "Asia", "Pola", "Asia"),

    ])
    class StudentParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_edit_class(self):
            self.assertIn(self.tmp.editStudent(self.id, self.name, self.surname, self.new_name, self.new_surname)[0][1],
                          self.expected)

    @parameterized_class(("id", "name", "surname", "new_name", "new_surname", "expected"), [
        (2, "Aneta", "Czarna", "Asia", "Pola", "There_is_not_such_student"),

    ])
    class StudentParameterizedExceptionsPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_edit_exception_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.editStudent, self.id, self.name, self.surname,
                                   self.new_name, self.new_surname)

    @parameterized_class(("id", "name", "surname", "new_name", "new_surname", "expected"), [
        (2, "Marcel", "Bialy", None, "Pola", "Bad_type_newName_or_newSurname"),
    ])
    class StudentParameterizedErrorsPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_edit_type_error_class(self):
            self.assertRaisesRegex(TypeError, self.expected, self.tmp.editStudent, self.id, self.name, self.surname,
                                   self.new_name, self.new_surname)


if __name__ == '__main__':
    unittest.main()
