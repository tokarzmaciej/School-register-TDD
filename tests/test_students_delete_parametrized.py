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

    @parameterized.expand([
        (3, "Kasia", "Polak", "There_is_not_such_student"),
    ])
    def test_student_delete_exceptions_expand(self, id, name, surname, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.deleteStudent, id, name, surname)

    @parameterized_class(("id", "name", "surname", "expected"), [
        (1, "Kasia", "Polak", ('1', 'Kasia', 'Polak')),
    ])
    class StudentParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_delete_class(self):
            self.assertNotIn(self.tmp.deleteStudent(self.id, self.name, self.surname), self.expected)

    @parameterized_class(("id", "name", "surname", "expected"), [
        (3, "Kasia", "Polak", "There_is_not_such_student"),
    ])
    class StudentParameterizedExceptionsPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Students()

        def test_student_delete_exception_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.deleteStudent, self.id, self.name, self.surname)


if __name__ == '__main__':
    unittest.main()
