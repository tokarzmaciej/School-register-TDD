import unittest
from src.remark import *


class RemarkEditParameterizedFile(unittest.TestCase):
    def setUp(self):
        self.tmp = Remarks()

    def test_edit_remark_name_from_file(self):
        fileTest = open("data/test_remark_edit_name.txt")
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6 = (
                    data[0], data[1], data[2], data[3], data[4], data[5].strip("\n"))
                self.assertIn(inp6, self.tmp.editRemarkName(inp1, inp2, inp3, inp4, inp5)[1])

        fileTest.close()

    def test_edit_remark_description_from_file(self):
        fileTest = open("data/test_remark_edit_description.txt")
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6 = (
                    data[0], data[1], data[2], data[3], data[4], data[5].strip("\n"))
                self.assertIn(inp6, self.tmp.editRemarkDescription(inp1, inp2, inp3, inp4, inp5))

        fileTest.close()

    def test_edit_remark_name_exceptions_from_file(self):
        fileTest = open("data/test_remark_edit_name_exceptions.txt")
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6 = (
                    data[0], data[1], data[2], data[3], data[4], data[5].strip("\n"))
                self.assertRaisesRegex(Exception, inp6, self.tmp.editRemarkName, inp1, inp2, inp3, inp4, inp5)

        fileTest.close()

    def test_edit_remark_description_exceptions_from_file(self):
        fileTest = open("data/test_remark_edit_description_exceptions.txt")
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6 = (
                    data[0], data[1], data[2], data[3], data[4], data[5].strip("\n"))
                self.assertRaisesRegex(Exception, inp6, self.tmp.editRemarkDescription, inp1, inp2, inp3, inp4, inp5)


if __name__ == '__main__':
    unittest.main()
