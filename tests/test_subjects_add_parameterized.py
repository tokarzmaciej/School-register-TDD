import unittest
from src.subjects import Subjects
from parameterized import parameterized, parameterized_class


class SubjectsAddParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Subjects()

    @parameterized.expand([
        (2, "Beata", "Jankowska", "english", {'subjects': {"english": {}}, 'remarks': {}}),
    ])
    def test_add_subjects_positive_expand(self, id, name, surname, name_subject, expected):
        self.assertEqual(self.tmp.addSubject(id, name, surname, name_subject), expected)

    @parameterized.expand([
        (12, "Zosia", "Kucharska", "math", "There_is_not_such_student"),
    ])
    def test_add_subjects_exceptions_expand(self, id, name, surname, name_subject, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.addSubject, id, name, surname, name_subject)

    @parameterized.expand([
        (2, "Beata", "Jankowska", True, "Bad_type_subject_name"),
    ])
    def test_add_subjects_type_errors(self, id, name, surname, name_subject, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.addSubject, id, name, surname, name_subject)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (2, "Beata", "Jankowska", "english", {'subjects': {"english": {}}, 'remarks': {}}),

    ])
    class SubjectsAddParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects()

        def test_add_subjects_positive_class(self):
            self.assertEqual(self.tmp.addSubject(self.id, self.name, self.surname, self.name_subject), self.expected)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (12, "Zosia", "Kucharska", "math", "There_is_not_such_student"),
    ])
    class SubjectsAddExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects()

        def test_add_subjects_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.addSubject, self.id, self.name, self.surname,
                                   self.name_subject)

    @parameterized_class(("id", "name", "surname", "name_subject", "expected"), [
        (2, "Beata", "Jankowska", True, "Bad_type_subject_name"),
    ])
    class SubjectsAddTypeErrorsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects()

        def test_add_subjects_type_error_class(self):
            self.assertRaisesRegex(TypeError, self.expected, self.tmp.addSubject, self.id, self.name, self.surname,
                                   self.name_subject)


if __name__ == '__main__':
    unittest.main()
