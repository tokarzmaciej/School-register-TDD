import pytest
from src.remark import Remarks


def test_add_remark_positive():
    result = {'volunteering': 'cleaning_the_environment'}
    assert Remarks().addRemark(2, "Beata", "Jankowska", "volunteering", "cleaning_the_environment") == result


def test_add_remark_already_exists():
    with pytest.raises(Exception):
        Remarks().addRemark(8, "Konrad", "Piasek", "competition", "first place")


def test_add_remark_lack_student():
    with pytest.raises(Exception):
        Remarks().addRemark(10, "Gosia", "Rosa", "help", "preparing_appeal")
