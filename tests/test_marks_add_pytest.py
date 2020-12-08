import pytest
from src.marks import Marks
from src.exampleData import Data


def test_add_mark_positive():
    result = ('test', 2)
    assert Marks(Data().example).addMark(4, "Alicja", "Zielonka", "math", "test", 2)[0] == result


def test_add_mark_mark_already_exists():
    with pytest.raises(Exception):
        Marks(Data().example).addMark(6, "Michal", "Krakowiak", "art", "singing_hymn", 3)


def test_add_mark_lack_subjects():
    with pytest.raises(Exception):
        Marks(Data().example).addMark(3, "Kacper", "Stoch", "geography", "activity", 5)


def test_add_mark_lack_student():
    with pytest.raises(Exception):
        Marks(Data().example).addMark(11, "Robert", "Perkoz", "english", "test-present-simple", 3)


def test_add_mark_range_mark():
    with pytest.raises(Exception):
        Marks(Data().example).addMark(4, "Alicja", "Zielonka", "math", "test", 7)


def test_add_mark_name_bad_type():
    with pytest.raises(TypeError):
        Marks(Data().example).addMark(5, "Piotr", "Fantazja", "math", "test", "1")
