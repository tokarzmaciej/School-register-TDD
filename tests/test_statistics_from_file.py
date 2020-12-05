import unittest
from src.statistics import *


class StatisticsParameterizedFile(unittest.TestCase):
    def test_average_subject_from_file(self):
        fileTest = open("data/test_statistics_subject.txt")
        tmp = Statistics()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, message = (data[0], data[1], data[2], data[3], int(data[4].strip("\n")))
                self.assertGreaterEqual(message, tmp.averageSubject(inp1, inp2, inp3, inp4)[1])
        fileTest.close()

    def test_average_subjects_from_file(self):
        fileTest = open("data/test_statistics_subjects.txt")
        tmp = Statistics()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, message = (data[0], data[1], data[2], int(data[3].strip("\n")))
                self.assertLessEqual(message, tmp.averageSubjects(inp1, inp2, inp3)[1])
        fileTest.close()

    def test_average_subject_from_file_exceptions(self):
        fileTest = open("data/test_statistics_subject_exceptions.txt")
        tmp = Statistics()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, inp4, message = (data[0], data[1], data[2], data[3], data[4].strip("\n"))
                self.assertRaisesRegex(Exception, message, tmp.averageSubject, inp1, inp2, inp3, inp4)
        fileTest.close()

    def test_average_subjects_from_file_exceptions(self):
        fileTest = open("data/test_statistics_subjects_exceptions.txt")
        tmp = Statistics()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp1, inp2, inp3, message = (data[0], data[1], data[2], data[3].strip("\n"))
                self.assertRaisesRegex(Exception, message, tmp.averageSubjects, inp1, inp2, inp3)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
