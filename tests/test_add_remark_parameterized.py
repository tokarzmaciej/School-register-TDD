import unittest
from src.remark import Remarks
from parameterized import parameterized, parameterized_class
from src.exampleData import Data


class RemarksAddParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Remarks(Data().example)

    @parameterized.expand([
        (2, "Beata", "Jankowska", "volunteering", "cleaning_the_environment",
         {'volunteering': 'cleaning_the_environment'}),
    ])
    def test_add_remark_positive_expand(self, id_student, name, surname, name_remark, description_remark, expected):
        self.assertEqual(expected, self.tmp.addRemark(id_student, name, surname, name_remark, description_remark))

    @parameterized.expand([
        (8, "Konrad", "Piasek", "competition", "first place", "This_remark_already_exists"),
        (10, "Gosia", "Rosa", "help", "preparing_appeal", "There_is_not_such_student")
    ])
    def test_add_remark_exceptions_expand(self, id_student, name, surname, name_remark, description_remark, expected):
        self.assertRaisesRegex(Exception, expected, self.tmp.addRemark, id_student, name, surname, name_remark,
                               description_remark)

    @parameterized_class(("id", "name", "surname", "name_remark", "description_remark", "expected"), [
        (2, "Beata", "Jankowska", "volunteering", "cleaning_the_environment",
         {'volunteering': 'cleaning_the_environment'})
    ])
    class RemarkAddParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Remarks(Data().example)

        def test_add_remark_positive_class(self):
            self.assertEqual(self.tmp.addRemark(self.id, self.name, self.surname, self.name_remark,
                                                self.description_remark), self.expected)

    @parameterized_class(("id", "name", "surname", "name_remark", "description_remark", "expected"), [
        (8, "Konrad", "Piasek", "competition", "first place", "This_remark_already_exists"),
        (10, "Gosia", "Rosa", "help", "preparing_appeal", "There_is_not_such_student")
    ])
    class RemarkAddExceptionsParameterizedPackageClass(unittest.TestCase):
        def setUp(self):
            self.tmp = Remarks(Data().example)

        def test_add_remark_exceptions_class(self):
            self.assertRaisesRegex(Exception, self.expected, self.tmp.addRemark, self.id, self.name, self.surname,
                                   self.name_remark, self.description_remark)


if __name__ == '__main__':
    unittest.main()
