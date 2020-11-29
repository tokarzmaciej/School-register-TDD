import unittest
from assertpy import assert_that
from src.students import Students
from key_generator.key_generator import generate


class StudentsAssertPyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Students()

    def test_edit_student_positive(self):
        self.temp.addStudent(1, "Ala", "Kot", "w")
        self.temp.addStudent(2, "Kasia", "Pola", "a")
        self.temp.addStudent(3, "Ola", "Fiolek", "a")
        assert_that(self.temp.editStudent(2, "Kasia", "Pola", "Asia", "Pola")[0][1]) \
            .contains('Asia')

    def test_edit_lack_student(self):
        self.temp.addStudent(1, "Ala", "Poziomka", "w")
        self.temp.addStudent(2, "Marcel", "Biala", "a")
        assert_that(self.temp.editStudent) \
            .raises(Exception) \
            .when_called_with(2, "Aneta", "Czarna", "Asia", "Pola")

    def test_edit_type_error(self):
        self.temp.addStudent(1, "Ala", "Poziomka", "w")
        self.temp.addStudent(2, "Marcel", "Bialy", "a")
        assert_that(self.temp.editStudent) \
            .raises(TypeError) \
            .when_called_with(2, "Marcel", "Bialy", None, "Pola")

    def test_delete_lack_student(self):
        self.temp.addStudent(1, "Kasia", "Polak", "w")
        self.temp.addStudent(2, "Kacper", "Stoch", "a")
        assert_that(self.temp.deleteStudent) \
            .raises(Exception) \
            .when_called_with(3, "Kasia", "Polak")

    def test_delete_student(self):
        self.temp.addStudent(1, "Kasia", "Polak", "w")
        self.temp.addStudent(2, "Kacper", "Stoch", "a")
        assert_that(self.temp.deleteStudent(1, "Kasia", "Polak")) \
            .is_not_empty() \
            .is_length(1)

    def test_add_the_same_students(self):
        self.temp.addStudent(2, "Beata", "Jankowska", "w")
        assert_that(self.temp.addStudent) \
            .raises(Exception) \
            .when_called_with(2, "Beata", "Jankowska", "a")

    def test_add_few_students(self):
        self.temp.addStudent(generate().get_key(), "Ala", "Kot", "w")
        self.temp.addStudent(generate().get_key(), "Agata", "Kwiatek", "a")
        assert_that(self.temp.addStudent(generate().get_key(), "Piotr", "Lewandowski", "a")) \
            .is_length(3)

    def test_add_student_positive(self):
        result = ('Add student', 'Adam', 'Nowak', {'subjects': {}, 'remarks': {}})
        assert_that(self.temp.addStudent(2, "Adam", "Nowak", "w")) \
            .is_equal_to(result)

    def test_add_student_bad_option(self):
        assert_that(self.temp.addStudent) \
            .raises(Exception) \
            .when_called_with(2, "Jan", "Kowalski", "g")

    def test_add_student_surname_bad_type(self):
        assert_that(self.temp.addStudent) \
            .raises(TypeError) \
            .when_called_with(2, "Jan", 2, "w")

    def test_add_student_name_bad_type(self):
        assert_that(self.temp.addStudent) \
            .raises(TypeError) \
            .when_called_with(2, True, "Kowalski", "w")

    def tearDown(self):
        self.temp = None
