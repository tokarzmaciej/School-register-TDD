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
    def test_student_add_expand(self, id_student, name, surname, expected):
        self.assertEqual(self.tmp.addStudent(id_student, name, surname), expected)

    @parameterized.expand([
        (2, "Beata", "Jankowska", "This_id_already_exists"),
    ])
    def test_student_add_exceptions_expand(self, id_student, name, surname, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.addStudent, id_student, name, surname)

    @parameterized.expand([
        (generate().get_key(), "Jan", 2, "Bad_type_name_or_surname"),
        (generate().get_key(), True, "Kowalski", "Bad_type_name_or_surname")
    ])
    def test_student_add_type_error_expand(self, id_student, name, surname, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.addStudent, id_student, name, surname)

    @parameterized_class(("id", "name", "surname", "expected"), [
        (generate().get_key(), "Adam", "Nowak", ('Add student', 'Adam', 'Nowak', {'subjects': {}, 'remarks': {}})),

    ])
    class StudentParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_add_class(self):
            self.assertEqual(self.tmp.addStudent(self.id, self.name, self.surname), self.expected)

    @parameterized_class(("id", "name", "surname", "expected"), [
        (2, "Beata", "Jankowska", "This_id_already_exists"),
    ])
    class StudentParameterizedExceptionsPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_add_exception_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.addStudent, self.id, self.name, self.surname)

    @parameterized_class(("id", "name", "surname", "expected"), [
        (generate().get_key(), "Jan", 2, "Bad_type_name_or_surname"),
    ])
    class StudentParameterizedErrorPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_add_type_error_class(self):
            self.assertRaisesRegex(TypeError, self.expected, self.tmp.addStudent, self.id, self.name, self.surname)


if __name__ == '__main__':
    unittest.main()
