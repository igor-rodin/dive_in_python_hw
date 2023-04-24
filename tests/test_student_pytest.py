import sys

sys.path.append("../homeworks")

import pytest

from student import Student


@pytest.fixture
def student():
    return Student("Иван", "Иванович", "Иванов")


def test_first_name(student):
    assert student.first_name == "Иван"


def test_middle_name(student):
    assert student.middle_name == "Иванович"


def test_last_name(student):
    assert student.last_name == "Иванов"


def test_name_is_title():
    with pytest.raises(ValueError):
        Student("иван", "Иванович", "Иванов")


def test_name_is_only_letters():
    with pytest.raises(ValueError):
        Student("Иван", "Иванович", "Иванов123")


def test_subjects(student):
    assert student.subjects == ("математика", "физика", "алгоритмы")


def test_validate_mark_raise(student):
    with pytest.raises(ValueError):
        student.validate_mark(20, min_mark=0, max_mark=5)


def test_add_mark(student):
    student.set_subject_mark("физика", 4)
    assert student.perfomance_journal == {
        "математика": {
            "marks": [],
            "test_marks": [],
            "avg_mark": None,
            "avg_test_mark": None,
        },
        "физика": {
            "marks": [4],
            "test_marks": [],
            "avg_mark": 4.0,
            "avg_test_mark": None,
        },
        "алгоритмы": {
            "marks": [],
            "test_marks": [],
            "avg_mark": None,
            "avg_test_mark": None,
        },
        "total_avg_mark": 1.3333333333333333,
        "total_avg_test_mark": None,
    }


if __name__ == "__main__":
    pytest.main(["-v", "tests/test_student_pytest.py"])
