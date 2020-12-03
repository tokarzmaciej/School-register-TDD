import unittest
from src.students import *


class StudentsParameterizedFile(unittest.TestCase):

    def test_student_add_from_file(self):
        fileTest = open("data/test_students_add.txt")
        tmpStudents = Students()
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


if __name__ == '__main__':
    unittest.main()
