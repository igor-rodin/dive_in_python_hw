'''Домашнее задание'''
import os
from pathlib import Path

__all__ = ['group_rename']


def __rename_file(file: Path, target_ext: str, range: tuple[int, int],
                  counter: int, counter_digits: int, pref_name: str = '') -> None:
    '''
    Переимеменовывает файл
    '''
    *_, file_name_with_ext = str(file).split('/')
    orig_name = file_name_with_ext[:file_name_with_ext.rfind('.')]
    if pref_name:
        pref_name = f'_{pref_name}'
    new_name = f'{orig_name[range[0]: range[1]]}{pref_name}_{counter:0>{counter_digits}}.{target_ext}'
    old = Path(file_name_with_ext)
    old.replace(Path.cwd() / new_name)


def group_rename(source_ext: str, target_ext: str, range: tuple[int, int],
                 counter_digits: int, source_dir: str = '', pref_name: str = '') -> None:
    '''
    Переименовывает файлы c расширением source_ext находящиеся в директории source_dir.
    source_dir - абсолютный путь, target_ext - новое расширение
    '''
    source_dir = source_dir or Path.cwd()
    cur_dir = Path.cwd()
    os.chdir(source_dir)
    counter = 0
    for file in Path(source_dir).iterdir():
        _, ext = os.path.splitext(file)
        if ext[1:] == source_ext:
            counter += 1
            __rename_file(file, target_ext, range,
                          counter, counter_digits, pref_name)
    if source_dir != cur_dir:
        os.chdir(cur_dir)


if __name__ == '__main__':
    dir = Path.cwd() / 'tmp'
    group_rename('dt', 'dat', (0, 4), 2, dir, pref_name='current')
