import unittest
from src.students import *


class StudentsParameterizedFile(unittest.TestCase):

    def test_student_edit_from_file(self):
        fileTest = open("data/test_students_edit.txt")
        tmpStudents = Students()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6 = (
                    data[0], data[1], data[2], data[3], data[4], data[5].strip("\n"))
                self.assertIn(tmpStudents.editStudent(inp1, inp2, inp3, inp4, inp5)[0][1], inp6)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
