import unittest
from src.remark import Remarks
from parameterized import parameterized, parameterized_class
from src.exampleData import Data


class RemarksEditParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Remarks(Data().example)

    @parameterized.expand([
        (8, "Konrad", "Piasek", "disturbing_lesson", "disturbing_math_lesson", "math_lesson")
    ])
    def test_edit_remark_name_expand(self, id_student, name, surname, name_remark, new_name_remark, expected):
        self.assertIn(expected, self.tmp.editRemarkName(id_student, name, surname, name_remark, new_name_remark)[1])

    @parameterized.expand([
        (7, "Ewelina", "Swoboda", "competition", "second_place", "second")
    ])
    def test_edit_remark_description_expand(self, id_student, name, surname, name_remark, new_description_remark,
                                            expected):
        self.assertIn(expected,
                      self.tmp.editRemarkDescription(id_student, name, surname, name_remark, new_description_remark))

    @parameterized.expand([
        (1, "Kasia", "Polak", "volunteering", "helping", "Student_not_have_this_remark"),
        (15, "Wiktor", "Nowak", "competition", "football_competition", "There_is_not_such_student")
    ])
    def test_edit_remark_name_exceptions_expand(self, id_student, name, surname, name_remark, new_name_remark,
                                                expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.editRemarkName, id_student, name, surname, name_remark,
                               new_name_remark)

    @parameterized.expand([
        (3, "Kacper", "Stoch", "volunteering", "helping_an_elderly_person", "Student_not_have_this_remark"),
        (14, "Julka", "Ostrowska", "competition", "first_place", "There_is_not_such_student")
    ])
    def test_edit_remark_description_exceptions_expand(self, id_student, name, surname, name_remark,
                                                       new_description_remark,
                                                       expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.editRemarkDescription, id_student, name, surname,
                               name_remark,
                               new_description_remark)

    @parameterized_class(("id", "name", "surname", "name_remark", "new_name_remark", "expected"), [
        (8, "Konrad", "Piasek", "disturbing_lesson", "disturbing_math_lesson", "math_lesson")
    ])
    class RemarkEditNameParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Remarks(Data().example)

        def test_edit_remark_name_class(self):
            self.assertIn(self.expected, self.tmp.editRemarkName(self.id, self.name, self.surname, self.name_remark,
                                                                 self.new_name_remark)[1])

    @parameterized_class(("id", "name", "surname", "name_remark", "new_description_remark", "expected"), [
        (7, "Ewelina", "Swoboda", "competition", "second_place", "second")
    ])
    class RemarkEditDescriptionParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Remarks(Data().example)

        def test_edit_remark_description_class(self):
            self.assertIn(self.expected,
                          self.tmp.editRemarkDescription(self.id, self.name, self.surname, self.name_remark,
                                                         self.new_description_remark))

    @parameterized_class(("id", "name", "surname", "name_remark", "new_name_remark", "expected"), [
        (1, "Kasia", "Polak", "volunteering", "helping", "Student_not_have_this_remark"),
        (15, "Wiktor", "Nowak", "competition", "football_competition", "There_is_not_such_student")
    ])
    class RemarkEditNameExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Remarks(Data().example)

        def test_edit_remark_name_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.editRemarkName, self.id, self.name, self.surname,
                                   self.name_remark,
                                   self.new_name_remark)

    @parameterized_class(("id", "name", "surname", "name_remark", "new_description_remark", "expected"), [
        (3, "Kacper", "Stoch", "volunteering", "helping_an_elderly_person", "Student_not_have_this_remark"),
        (14, "Julka", "Ostrowska", "competition", "first_place", "There_is_not_such_student")
    ])
    class RemarkEditDescriptionExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Remarks(Data().example)

        def test_edit_remark_description_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.editRemarkDescription, self.id, self.name,
                                   self.surname, self.name_remark, self.new_description_remark)


if __name__ == '__main__':
    unittest.main()
