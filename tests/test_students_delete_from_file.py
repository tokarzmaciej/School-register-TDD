import unittest
from src.students import *


class StudentsParameterizedFile(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_student_delete_from_file(self):
        fileTest = open("data/test_students_delete.txt")
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6 = (
                    data[0], data[1], data[2], data[3], data[4], data[5].strip("\n"))
                self.assertNotIn(self.temp.deleteStudent(inp1, inp2, inp3), (inp4, inp5, inp6))
        fileTest.close()

    def test_student_delete_from_file_exceptions(self):
        fileTest = open("data/test_students_delete_exception.txt")
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, message = (data[0], data[1], data[2], data[3].strip("\n"))
                self.assertRaisesRegex(Exception, message, self.temp.deleteStudent, inp1, inp2, inp3)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
