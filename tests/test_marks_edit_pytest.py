import pytest
from src.marks import Marks
from src.exampleData import Data


def test_edit_mark_positive():
    result = ('quiz', 4)
    assert Marks(Data().example).editMark(7, "Ewelina", "Swoboda", "physics", "quiz", 4)[2] == result


def test_edit_mark_lack_mark():
    with pytest.raises(Exception):
        Marks(Data().example).editMark(6, "Michal", "Krakowiak", "math", "exam", 3)


def test_edit_mark_lack_subjects():
    with pytest.raises(Exception):
        Marks(Data().example).editMark(4, "Alicja", "Zielonka", "history", "test", 3)


def test_edit_mark_lack_student():
    with pytest.raises(Exception):
        Marks(Data().example).editMark(10, "Ewa", "Piech", "english", "quiz", 5)


def test_edit_mark_grade_bad_type():
    with pytest.raises(TypeError):
        Marks(Data().example).editMark(7, "Ewelina", "Swoboda", "physics", "quiz", False)
