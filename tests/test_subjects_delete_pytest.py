import pytest
from src.subjects import Subjects


def test_delete_subject_positive():
    result = {'subjects': {'history': {}, 'art': {}}, 'remarks': {}}
    assert Subjects().deleteSubject(5, "Piotr", "Fantazja", "math") == result


def test_delete_subject_to_lack_subjects():
    with pytest.raises(Exception):
        Subjects().deleteSubject(5, "Piotr", "Fantazja", "geography")


def test_delete_subject_name_bad_type():
    with pytest.raises(TypeError):
        Subjects().deleteSubject(5, "Piotr", "Fantazja", 1234)


def test_delete_subject_to_lack_student():
    with pytest.raises(Exception):
        Subjects().deleteSubject(10, "Ania", "Zegan", "english")
