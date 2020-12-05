import unittest
from src.remark import *


class RemarkAddParameterizedFile(unittest.TestCase):
    def test_add_remark_from_file(self):
        fileTest = open("data/test_add_remark.txt")
        tmp = Remarks()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, inp5, inp6, imp7 = (
                    data[0], data[1], data[2], data[3], data[4], data[5], data[6].strip("\n"))
                self.assertEqual({'volunteering': 'cleaning_the_environment'},
                                 tmp.addRemark(inp1, inp2, inp3, inp4, inp5))
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
