import unittest
from src.subjects import Subjects
from parameterized import parameterized, parameterized_class
from src.exampleData import Data


class SubjectsDeleteParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Subjects(Data().example)

    @parameterized.expand([
        (5, "Piotr", "Fantazja", "math", {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}),
    ])
    def test_delete_subjects_positive_expand(self, id_student, name, surname, name_subject, expected):
        self.assertEqual(self.tmp.deleteSubject(id_student, name, surname, name_subject), expected)

    @parameterized.expand([
        (10, "Ania", "Zegan", "english", "There_is_not_such_student"),
        (5, "Piotr", "Fantazja", "geography", "Student_not_have_this_subject")
    ])
    def test_delete_subjects_exceptions_expand(self, id_student, name, surname, name_subject, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.deleteSubject, id_student, name, surname, name_subject)

    @parameterized.expand([
        (5, "Piotr", "Fantazja", 1234, "Bad_type_subject_name"),
    ])
    def test_delete_subjects_type_errors(self, id_student, name, surname, name_subject, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.deleteSubject, id_student, name, surname, name_subject)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (5, "Piotr", "Fantazja", "math", {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}),

    ])
    class SubjectsDeleteParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects(Data().example)

        def test_delete_subjects_positive_class(self):
            self.assertEqual(self.tmp.deleteSubject(self.id, self.name, self.surname, self.name_subject), self.expected)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (10, "Ania", "Zegan", "english", "There_is_not_such_student"),
        (5, "Piotr", "Fantazja", "geography", "Student_not_have_this_subject")
    ])
    class SubjectsDeleteExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects(Data().example)

        def test_delete_subjects_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.deleteSubject, self.id, self.name, self.surname,
                                   self.name_subject)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (5, "Piotr", "Fantazja", 1234, "Bad_type_subject_name"),
    ])
    class SubjectsDeleteTypeErrorsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects(Data().example)

        def test_delete_subjects_type_errors_class(self):
            self.assertRaisesRegex(TypeError, self.expected, self.tmp.deleteSubject, self.id, self.name, self.surname,
                                   self.name_subject)


if __name__ == '__main__':
    unittest.main()
