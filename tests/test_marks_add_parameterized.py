import unittest
from src.marks import Marks
from parameterized import parameterized, parameterized_class


class MarksAddParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Marks()

    @parameterized.expand([
        (4, "Alicja", "Zielonka", "math", "test", 2, ('test', 2)),
    ])
    def test_add_mark_positive_expand(self, id_student, name, surname, name_subject, name_mark, grade, expected):
        self.assertIn(expected, self.tmp.addMark(id_student, name, surname, name_subject, name_mark, grade))

    @parameterized.expand([
        (4, "Alicja", "Zielonka", "math", "test", 7, "Bad_range_marks"),
        (11, "Robert", "Perkoz", "english", "test-present-simple", 3, "There_is_not_such_student"),
        (3, "Kacper", "Stoch", "geography", "activity", 5, "Student_not_have_this_subject"),
        (6, "Michal", "Krakowiak", "art", "singing_hymn", 3, "This_mark_already_exists")
    ])
    def test_add_mark_exceptions_expand(self, id_student, name, surname, name_subject, name_mark, grade, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.addMark, id_student, name, surname, name_subject,
                               name_mark, grade)

    @parameterized.expand([
        (5, "Piotr", "Fantazja", "math", "test", "1", "Bad_type_grade"),
    ])
    def test_add_mark_type_errors_expand(self, id_student, name, surname, name_subject, name_mark, grade, expected):
        self.assertRaisesRegex(TypeError, expected, self.tmp.addMark, id_student, name, surname, name_subject,
                               name_mark, grade)

    @parameterized_class(("id", "name", "surname", "name_subject", "new_mark", "grade", "expected"), [
        (4, "Alicja", "Zielonka", "math", "test", 2, ('test', 2)),

    ])
    class MarksAddParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Marks()

        def test_add_mark_positive_class(self):
            self.assertIn(self.expected, self.tmp.addMark(self.id, self.name, self.surname, self.name_subject,
                                                          self.new_mark, self.grade))

    @parameterized_class(("id", "name", "surname", "name_subject", "new_mark", "grade", "expected"), [
        (4, "Alicja", "Zielonka", "math", "test", 7, "Bad_range_marks"),
        (11, "Robert", "Perkoz", "english", "test-present-simple", 3, "There_is_not_such_student"),
        (3, "Kacper", "Stoch", "geography", "activity", 5, "Student_not_have_this_subject"),
        (6, "Michal", "Krakowiak", "art", "singing_hymn", 3, "This_mark_already_exists")
    ])
    class MarksAddExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Marks()

        def test_add_mark_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.addMark, self.id, self.name, self.surname,
                                   self.name_subject, self.new_mark, self.grade)

    @parameterized_class(("id", "name", "surname", "name_subject", "new_mark", "grade", "expected"), [
        (5, "Piotr", "Fantazja", "math", "test", "1", "Bad_type_grade"),

    ])
    class MarksAddTypeErrorsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Marks()

        def test_add_mark_type_errors_class(self):
            self.assertRaisesRegex(TypeError, self.expected, self.tmp.addMark, self.id, self.name, self.surname,
                                   self.name_subject, self.new_mark, self.grade)


if __name__ == '__main__':
    unittest.main()
