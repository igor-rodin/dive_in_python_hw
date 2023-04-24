from typing import Any
from string import ascii_letters
import random
from serialize.s_csv import read_l_csv
from serialize.s_json import write_json
import doctest


class TitleWord:
    """
    Класс дескриптор, контролирующий, что ФИО состоит только из букв и начинаеетсся с заглаавной буквы

    >>> tw = TitleWord()
    >>> tw.validate('Name')
    >>> tw.validate('name')
    Traceback (most recent call last):
    ...
    ValueError: ФИО должно быть с заглавной буквы
    >>> tw.validate('Name123')
    Traceback (most recent call last):
    ...
    ValueError: ФИО должно должно сотоять только из букв
    """

    RUS_LETTERS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    @classmethod
    def validate(cls, value: str) -> None:
        if not value.istitle():
            raise ValueError("ФИО должно быть с заглавной буквы")
        if len(value.strip(ascii_letters + cls.RUS_LETTERS)) != 0:
            raise ValueError("ФИО должно должно сотоять только из букв")

    def __set_name__(self, owner, name) -> None:
        self.name = "_" + name

    def __get__(self, instance, owner) -> Any:
        return getattr(instance, self.name)

    def __set__(self, instance, value) -> None:
        self.validate(value)
        setattr(instance, self.name, value)


class Student:
    """
    >>> st = Student('Иван', 'Иванович', 'Иванов')
    >>> st.first_name
    'Иван'
    >>> st.middle_name
    'Иванович'
    >>> st.last_name
    'Иванов'
    >>> st.subjects
    ('математика', 'физика', 'алгоритмы')
    """

    MIN_MARK = 2
    MAX_SUBJECT_MARK = 5
    MAX_TEST_MARK = 100

    first_name = TitleWord()
    middle_name = TitleWord()
    last_name = TitleWord()

    subjects = tuple()

    def __init__(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        subjects_file="subjects.csv",
    ) -> None:
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        self.subjects = tuple(sub[0] for sub in read_l_csv(subjects_file))
        self.perfomance_journal = {
            subject: {
                "marks": [],
                "test_marks": [],
                "avg_mark": None,
                "avg_test_mark": None,
            }
            for subject in self.subjects
        }
        self.perfomance_journal["total_avg_mark"] = None
        self.perfomance_journal["total_avg_test_mark"] = None

    def __str__(self) -> str:
        """Отображает информацию об успеваемости студента"""
        line = "-" * 70
        subject_stat = "\n".join(
            [
                f"{sub:<20}\t{self.perfomance_journal[sub]['avg_mark']:<15}\t{self.perfomance_journal[sub]['avg_test_mark']:<15}"
                for sub in self.subjects
            ]
        )
        title = "{:^20}\t{:^15}\t{:^15}\n{}".format(
            "Предмет", "Средняя оценка", "Средняя оценка за тесты", line
        )
        total_avgs = f"\t{self.perfomance_journal['total_avg_mark']:3.1f}\t{self.perfomance_journal['total_avg_test_mark']:3.1f}"
        footer = f"Итого по всем предметам:\nСредняя оценка\tСредняя оценка за тесты\n{line}\n{total_avgs}\n{line}"
        return f"{line}\nСтудент: {self.first_name} {self.middle_name} {self.last_name}\n{line}\n{title}\n{subject_stat}\n{line}\n{footer}"

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self.first_name}, {self.middle_name}, {self.last_name})"

    @staticmethod
    def validate_mark(value: int, min_mark: int = 0, max_mark: int = 5) -> None:
        """Проверяет, что оценка в диапазоне (min_mark - max_mark)"""

        if type(value) is not int or value < min_mark or value > max_mark:
            raise ValueError(
                f"Оценка должна быть целым числом в диапазоне {min_mark} - {max_mark}"
            )

    def set_subject_mark(self, subject: str, mark: int, is_test=False):
        """Добавляет оценку по предмету или тесту в журнал"""

        if subject not in self.subjects:
            raise ValueError("Предмет не входит в программу обучения")

        self.validate_mark(
            mark, max_mark=self.MAX_TEST_MARK
        ) if is_test else self.validate_mark(mark, min_mark=self.MIN_MARK)

        subject_mark = "test_marks" if is_test else "marks"
        self.perfomance_journal[subject][subject_mark].append(mark)
        self._update_subject_stat(subject, is_test)
        self._update_total_avg(is_test)

    def _update_subject_stat(self, subject: str, is_test: bool = False) -> None:
        """Обновляет средние оценки по предмету"""
        subject_marks, avg_subject_mark = (
            ("test_marks", "avg_test_mark") if is_test else ("marks", "avg_mark")
        )
        self.perfomance_journal[subject][avg_subject_mark] = sum(
            self.perfomance_journal[subject][subject_marks]
        ) / len(self.perfomance_journal[subject][subject_marks])

    def _update_total_avg(self, is_test):
        """Обновляет общую среднюю оценку по всем предметам"""
        avg_subject_mark, total_avg_mark = (
            ("avg_test_mark", "total_avg_test_mark")
            if is_test
            else ("avg_mark", "total_avg_mark")
        )

        total_avg = 0.0
        for key, val in self.perfomance_journal.items():
            if key not in ("total_avg_test_mark", "total_avg_mark"):
                for sub_key, sub_val in val.items():
                    if sub_key == avg_subject_mark:
                        if sub_val is not None:
                            total_avg += sub_val
        self.perfomance_journal[total_avg_mark] = total_avg / len(self.subjects)

    def export_journal_to_json(
        self, file_name: str = "perfomance_journal", preaty_print: bool = False
    ):
        """Экспортирует журнал успеваемости в json файл"""
        export_file = f"{file_name}.json"
        write_json(self.perfomance_journal, export_file, preaty_print)


def fill_random_journal(st: Student, tests_count: int) -> None:
    """Заполняет журнал успеваемости случайными оценками для тестирования"""
    for sub in st.subjects:
        for _ in range(tests_count):
            st.set_subject_mark(sub, random.randrange(2, 5 + 1))
        for _ in range(tests_count // 8):
            st.set_subject_mark(sub, random.randrange(100 + 1), is_test=True)


def test_student():
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    test_student()
    st = Student("Иван", "Петрович", "Кузнецов")
    st.set_subject_mark("физика", 4)
    print(st.perfomance_journal)
    # fill_random_journal(st, tests_count=20)
    # st.export_journal_to_json()
    # print(f"{st = }")
    # print(st)
