import unittest
from src.marks import Marks
from parameterized import parameterized, parameterized_class


class MarksEditParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Marks()

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", "physics", "quiz", 4, ('quiz', 4)),
    ])
    def test_edit_mark_positive_expand(self, id, name, surname, name_subject, name_mark, grade, expected):
        self.assertIn(expected, self.tmp.editMark(id, name, surname, name_subject, name_mark, grade))

    @parameterized.expand([
        (10, "Ewa", "Piech", "english", "quiz", 5, "There_is_not_such_student"),
        (4, "Alicja", "Zielonka", "history", "test", 3, "Student_not_have_this_subject"),
        (6, "Michal", "Krakowiak", "math", "exam", 3, "There_is_not_such_mark")
    ])
    def test_edit_mark_exceptions_expand(self, id, name, surname, name_subject, name_mark, grade, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.editMark, id, name, surname, name_subject, name_mark,
                               grade)


if __name__ == '__main__':
    unittest.main()
