import pytest
from src.subjects import Subjects


def test_edit_subject_positive():
    result = "history_art"
    assert Subjects().editSubject(6, "Michal", "Krakowiak", "art", "history_art")[2] == result


def test_edit_subject_to_lack_subjects():
    with pytest.raises(Exception):
        Subjects().editSubject(4, "Alicja", "Zielonka", "history", "world-history")


def test_edit_subject_to_lack_student():
    with pytest.raises(Exception):
        Subjects().editSubject(2, "Grzegorz", "Kowalczyk", "english", "primary_english")


def test_edit_subject_name_bad_type():
    with pytest.raises(TypeError):
        Subjects().editSubject(5, "Piotr", "Fantazja", "history", False)
