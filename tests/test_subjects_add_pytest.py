import pytest
from src.subjects import Subjects


def test_add_subjects_positive():
    result = {'subjects': {"english": {}}, 'remarks': {}}
    assert Subjects().addSubject(2, "Beata", "Jankowska", "english") == result


def test_add_subject_to_lack_student():
    with pytest.raises(Exception):
        Subjects().addSubject(12, "Zosia", "Kucharska", "math")


def test_add_subject_name_subject_bad_type():
    with pytest.raises(Exception):
        Subjects().addSubject(2, "Beata", "Jankowska", True)
