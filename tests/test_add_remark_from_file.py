import unittest
from src.remark import *
from src.exampleData import Data


class RemarkAddParameterizedFile(unittest.TestCase):
    def test_add_remark_from_file(self):
        fileTest = open("data/test_add_remark.txt")
        tmp = Remarks(Data().example)
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6, inp7 = (
                    data[0], data[1], data[2], data[3], data[4], data[5], data[6].strip("\n"))
                self.assertEqual({inp6: inp7},
                                 tmp.addRemark(inp1, inp2, inp3, inp4, inp5))
        fileTest.close()

    def test_add_remark_exceptions_from_file(self):
        fileTest = open("data/test_add_remark_exceptions.txt")
        tmp = Remarks(Data().example)
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6 = (
                    data[0], data[1], data[2], data[3], data[4], data[5].strip("\n"))
                self.assertRaisesRegex(Exception, inp6, tmp.addRemark, inp1, inp2, inp3, inp4, inp5)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
