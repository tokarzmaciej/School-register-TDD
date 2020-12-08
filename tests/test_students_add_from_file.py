import unittest
from src.students import *
from src.exampleData import Data


class StudentsParameterizedFile(unittest.TestCase):

    def test_student_add_from_file(self):
        fileTest = open("data/test_students_add.txt")
        tmpStudents = Students(Data().example)
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9 = (
                    data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8].strip("\n"))
                self.assertEqual(tmpStudents.addStudent(inp1, inp2, inp3),
                                 (inp4 + " " + inp5, inp6, inp7, {inp8: {}, inp9: {}}))
        fileTest.close()

    def test_student_add_from_file_exceptions(self):
        fileTest = open("data/test_students_add_exception.txt")
        tmpStudents = Students(Data().example)
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, message = (data[0], data[1], data[2], data[3].strip("\n"))
                self.assertRaisesRegex(Exception, message, tmpStudents.addStudent, inp1, inp2, inp3)
        fileTest.close()

    def test_student_add_from_file_type_error(self):
        fileTest = open("data/test_students_add_type_error.txt")
        tmpStudents = Students(Data().example)
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, message = (data[0], int(data[1]), bool(data[2]), data[3].strip("\n"))
                self.assertRaisesRegex(TypeError, message, tmpStudents.addStudent, inp1, inp2, inp3)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
