''' Задачи с семинара 7 '''

import math
import random
import os
from pathlib import Path

__all__ = ['fill_int_float', 'gen_names', 'gen_prod_names',
           'gen_files', 'gen_files_with_mul_ext', 'gen_files_to_dir', 'group_files']

__MIN_VALUE = -1000
__MAX_VALUE = 1000

__MIN_CHAR = 4
__MAX_CHAR = 7

__MIN_NAME_LENGTH = 6
__MAX_NAME_LENGTH = 30
__MIN_BYTES_COUNT = 256
__MAX_BYTES_COUNT = 4096
__FILES_COUNT = 42


def __gen_name(min_length: int = __MIN_NAME_LENGTH, max_length: int = __MAX_NAME_LENGTH, vowels_freq: int = 40) -> str:
    consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'l',
                  'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x')
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    name = []
    for _ in range(random.randrange(min_length, max_length)):
        name.append(random.choice(vowels)) if random.randrange(1,
                                                               100 // vowels_freq + 1) == 1 else name.append(random.choice(consonants))

    return ''.join(name)


def __move_to_group(group: str, file: Path) -> None:
    '''
    Перемещает файл file в директорию group относительно текущей директории
    '''
    cur_path = Path.cwd() / group
    if not Path(cur_path).is_dir():
        Path(cur_path).mkdir()
    *_, file_name = str(file).split('/')
    cur_file = Path(file_name)
    cur_file.replace(cur_path / cur_file)


def __group_file(file: Path) -> None:
    '''
    Определяет файл в категорию основываясь на его расширении
    '''
    group_exts = {'movie': ('mpeg4', 'mp4', 'avi', 'mov'), 'img': ('jpeg', 'bmp', 'tiff', 'png', 'jpg'),
                  'audio': ('ogg', 'mp3', 'wav'), 'text': ('txt', 'csv')}
    _, ext = os.path.splitext(file)
    ext = ext[1:]
    for group, exts in group_exts.items():
        if ext in exts:
            __move_to_group(group, file)
            return


# Задание No1
# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции


def fill_int_float(file: str, lines_count: int = 10) -> None:
    with open(file, mode='w', encoding='utf-8') as f:
        for _ in range(lines_count):
            int_num = random.randrange(__MIN_VALUE, __MAX_VALUE + 1)
            float_num = random.uniform(__MIN_VALUE, __MAX_VALUE)
            f.write(f"{int_num}|{float_num}\n")


# Задание No2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,состоять из 4-7 букв, среди которыхобязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл


def gen_names(file: str, word_count: int = 10) -> None:
    with open(file, mode='w', encoding='utf-8') as f:
        for _ in range(word_count):
            name = __gen_name(__MIN_CHAR, __MAX_CHAR + 1).capitalize()
            f.write(f"{name}\n")


# Задание No3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало


def gen_prod_names(file_num: str, file_names: str, file_res: str) -> None:
    def read_line(f) -> str:
        data = f.readline()
        if data == '':
            f.seek(0)
            data = f.readline()
        return data[:-1]

    with (open(file_num, 'r', encoding='utf-8') as f_num,
            open(file_names, 'r', encoding='utf-8') as f_names,
            open(file_res, 'w', encoding='utf-8') as f_res):
        len_num = sum(1 for _ in f_num)
        len_names = sum(1 for _ in f_names)
        for _ in range(max(len_num, len_names)):
            num1, num2 = read_line(f_num).split('|')
            product = int(num1) * float(num2)
            name = read_line(f_names)
            result = f'{name} {round(product)}' if product >= 0 else f'{name := name.upper()} {math.fabs(product):.2f}'
            f_res.write(f'{result}\n')


# Задание No4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


def gen_files(ext: str, target_dir: str = '', min_length: int = __MIN_NAME_LENGTH, max_length: int = __MAX_NAME_LENGTH,
              min_bytes: int = __MIN_BYTES_COUNT, max_bytes: int = __MAX_BYTES_COUNT,
              files_count: int = __FILES_COUNT) -> None:
    '''
    Создает files_count файлов с рпсшширением ext в директорию target_dir.
    Если target_dir не задана, файлы создаются в директории tmp внутри текущей директории
    '''
    for _ in range(files_count):
        file_name = f"{__gen_name(min_length, max_length)}.{ext}"
        if target_dir:
            if not Path(target_dir).is_dir():
                Path(target_dir).mkdir()
            file_name = target_dir / file_name
        else:
            file_name = Path.cwd() / 'tmp' / file_name

        count_bytes = random.randrange(min_bytes, max_bytes + 1)
        data = bytes(count_bytes)
        if not Path(file_name).is_file():
            with open(file_name, mode='+bw') as f:
                f.write(data)


# Задание No5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

def gen_files_with_mul_ext(exts: dict[str, int]) -> None:
    for ext, files_count in exts.items():
        gen_files(ext, files_count=files_count)


# Задание No6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

def gen_files_to_dir(exts: dict[str, int], target_dir: str = '') -> None:
    for ext, files_count in exts.items():
        gen_files(ext, target_dir, files_count=files_count)

# Задание No7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


def group_files(source_dir: str = '') -> None:
    '''
    Группирует файлы по категориям внутри source_dir.
    source_dir - абсолютный путь
    '''
    source_dir = source_dir or Path.cwd()
    cur_dir = Path.cwd()
    os.chdir(source_dir)
    for file in Path(source_dir).iterdir():
        __group_file(file)
    if source_dir != cur_dir:
        os.chdir(cur_dir)


if __name__ == '__main__':
    # fill_int_float('data_num.txt', 20)
    # gen_names('data_names.txt', 10)
    # gen_prod_names('data_num.txt', 'data_names.txt', 'data_sum.txt')
    # gen_files('dat', files_count=5)
    dir = Path.cwd() / 'tmp'
    gen_files_to_dir({'mp3': 2}, target_dir=dir)
    group_files(dir)
