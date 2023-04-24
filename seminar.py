import string

# Задание №1
# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.


def clean_str(text: str) -> str:
    """
    Удаляет из строки все символы, кроме латиского алфавита и пробелов

    >>> clean_str('binding class')
    'binding class'
    >>> clean_str('Binding Class')
    'binding class'
    >>> clean_str('binding: class!!')
    'binding class'
    >>> clean_str('пример - binding class')
    'binding class'
    >>> clean_str('Пример123 - Binding, Class!!')
    'binding class'
    """

    res_str = "".join(
        char for char in text if char in string.ascii_letters or char.isspace()
    )
    return res_str.strip().lower()


# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# - возврат строки без изменений
# - возврат строки с преобразованием регистра без потери символов
# - возврат строки с удалением знаков пунктуации
# - возврат строки с удалением букв других алфавитов
# - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

if __name__ == "__main__":
    # text = "Создайте функцию, которая To set up an instaаорпаnce of the binding class for use with a fragmentудаляет из текста все символы кроме букв латинского алфавита и пробелов."
    # print(clean_str(text))
    import doctest

    doctest.testmod(verbose=True)
