import unittest
from src.subjects import Subjects
from parameterized import parameterized, parameterized_class
from src.exampleData import Data


class SubjectsEditParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Subjects(Data().example)

    @parameterized.expand([
        (6, "Michal", "Krakowiak", "art", "history_art", "history_art"),
    ])
    def test_edit_subjects_positive_expand(self, id_student, name, surname, name_subject, new_name_subject, expected):
        self.assertIn(expected, self.tmp.editSubject(id_student, name, surname, name_subject, new_name_subject))

    @parameterized.expand([
        (2, "Grzegorz", "Kowalczyk", "english", "primary_english", "There_is_not_such_student"),
        (4, "Alicja", "Zielonka", "history", "world-history", "Student_not_have_this_subject")
    ])
    def test_edit_subjects_exceptions_expand(self, id_student, name, surname, name_subject, new_name_subject, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.editSubject, id_student, name, surname, name_subject,
                               new_name_subject)

    @parameterized.expand([
        (5, "Piotr", "Fantazja", "history", False, "Bad_type_new_subject_name"),
    ])
    def test_edit_subjects_type_errors_expand(self, id_student, name, surname, name_subject, new_name_subject,
                                              expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.editSubject, id_student, name, surname, name_subject,
                               new_name_subject)

    @parameterized_class(("id", "name", "surname", "name_subject", "new_name_subject", "expected"), [
        (6, "Michal", "Krakowiak", "art", "history_art", "history_art"),

    ])
    class SubjectsEditParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects(Data().example)

        def test_edit_subjects_positive_class(self):
            self.assertIn(self.expected, self.tmp.editSubject(self.id, self.name, self.surname, self.name_subject,
                                                              self.new_name_subject))

    @parameterized_class(("id", "name", "surname", "name_subject", "new_name_subject", "expected"), [
        (2, "Grzegorz", "Kowalczyk", "english", "primary_english", "There_is_not_such_student"),
        (4, "Alicja", "Zielonka", "history", "world-history", "Student_not_have_this_subject")
    ])
    class SubjectsEditExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects(Data().example)

        def test_edit_subjects_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.editSubject, self.id, self.name, self.surname,
                                   self.name_subject, self.new_name_subject)

    @parameterized_class(("id", "name", "surname", "name_subject", "new_name_subject", "expected"), [
        (5, "Piotr", "Fantazja", "history", False, "Bad_type_new_subject_name"),
    ])
    class SubjectsEditTypeErrorsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Subjects(Data().example)

        def test_edit_subjects_type_errors_class(self):
            self.assertRaisesRegex(TypeError, self.expected, self.tmp.editSubject, self.id, self.name, self.surname,
                                   self.name_subject, self.new_name_subject)


if __name__ == '__main__':
    unittest.main()
