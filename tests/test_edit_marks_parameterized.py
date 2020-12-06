import unittest
from src.marks import Marks
from parameterized import parameterized, parameterized_class


class MarksEditParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Marks()

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", "physics", "quiz", 4, ('quiz', 4)),
    ])
    def test_edit_mark_positive_expand(self, id_student, name, surname, name_subject, name_mark, grade, expected):
        self.assertIn(expected, self.tmp.editMark(id_student, name, surname, name_subject, name_mark, grade))

    @parameterized.expand([
        (10, "Ewa", "Piech", "english", "quiz", 5, "There_is_not_such_student"),
        (4, "Alicja", "Zielonka", "history", "test", 3, "Student_not_have_this_subject"),
        (6, "Michal", "Krakowiak", "math", "exam", 3, "There_is_not_such_mark")
    ])
    def test_edit_mark_exceptions_expand(self, id_student, name, surname, name_subject, name_mark, grade, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.editMark, id_student, name, surname, name_subject,
                               name_mark,
                               grade)

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", "physics", "quiz", False, "Bad_type_grade"),
    ])
    def test_edit_mark_type_errors_expand(self, id_student, name, surname, name_subject, name_mark, grade, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.editMark, id_student, name, surname, name_subject,
                               name_mark,
                               grade)

    @parameterized_class(("id", "name", "surname", "name_subject", "new_mark", "grade", "expected"), [
        (7, "Ewelina", "Swoboda", "physics", "quiz", 4, ('quiz', 4)),

    ])
    class MarksEditParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Marks()

        def test_edit_mark_positive_class(self):
            self.assertIn(self.expected, self.tmp.editMark(self.id, self.name, self.surname, self.name_subject,
                                                           self.new_mark, self.grade))

    @parameterized_class(("id", "name", "surname", "name_subject", "new_mark", "grade", "expected"), [
        (10, "Ewa", "Piech", "english", "quiz", 5, "There_is_not_such_student"),
        (4, "Alicja", "Zielonka", "history", "test", 3, "Student_not_have_this_subject"),
        (6, "Michal", "Krakowiak", "math", "exam", 3, "There_is_not_such_mark")
    ])
    class MarksEditExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Marks()

        def test_edit_mark_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.editMark, self.id, self.name, self.surname,
                                   self.name_subject, self.new_mark, self.grade)

    @parameterized_class(("id", "name", "surname", "name_subject", "new_mark", "grade", "expected"), [
        (7, "Ewelina", "Swoboda", "physics", "quiz", False, "Bad_type_grade"),
    ])
    class MarksEditTypeErrorsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Marks()

        def test_edit_mark_type_errors_class(self):
            self.assertRaisesRegex(TypeError, self.expected, self.tmp.editMark, self.id, self.name, self.surname,
                                   self.name_subject, self.new_mark, self.grade)


if __name__ == '__main__':
    unittest.main()
