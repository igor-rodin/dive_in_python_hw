
from typing import Any
from string import ascii_letters


class TitleWord:
    RUS_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    @classmethod
    def validate(cls, value: str):
        if not value.istitle():
            raise ValueError('ФИО должно быть с заглавной буквы')
        if len(value.strip(ascii_letters + cls.RUS_LETTERS)) != 0:
            raise ValueError('ФИО должно должно сотоять только из букв')

    def __set_name__(self, owner, name) -> None:
        self.name = '_' + name

    def __get__(self, instance, owner) -> Any:
        return getattr(instance, self.name)

    def __set__(self, instance, value) -> None:
        self.validate(value)
        setattr(instance, self.name, value)


class Student:
    first_name = TitleWord()
    middle_name = TitleWord()
    last_name = TitleWord()

    def __init__(self, first_name: str, middle_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'Студент: {self.first_name} {self.middle_name} {self.last_name}'


if __name__ == '__main__':
    st = Student('Игорь', 'Анатольевич', 'Родин')
    print(st)
