from src.service import *
from unittest.mock import *
from unittest import TestCase, main


class ServiceTest(TestCase):
    def test_export_first_student(self):
        test_object = Service()
        test_object.data = Mock(name="data")
        test_object.data = {}
        result = test_object.exportStudent(1, "Basia", "Kowalska", {}, {})
        self.assertEqual(True, result)

    def test_export_second_and_more_student(self):
        test_object = Service()
        test_object.data = Mock(name="data")
        test_object.data = {("1", "Basia", "Kowalska"): {"subjects": {}, "remarks": {}}}
        result = test_object.exportStudent(2, "Piotr", "Nowak", {}, {})
        self.assertEqual(True, result)

    def test_import_students(self):
        test_object = Service()
        test_object.data = Mock(name="data")
        test_object.data = {}
        test_object.exportStudent(1, "Basia", "Kowalska", {}, {})
        result = test_object.importStudents().keys()
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    main()
