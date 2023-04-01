from pathlib import Path
from enum import Enum
import serialize.s_json as s_json
import serialize.s_csv as s_csv
import serialize.s_pickle as s_pickle


class FileType(Enum):
    JSON = 1
    CSV = 2
    PICKLE = 3


def get_dir_stat(dir: str = '', file_type: FileType = FileType.JSON) -> None:
    '''
    Собирает статистику по директории dir c учетом вложенности и записывает
    результат в файлы формата json, csv, pickle. Имя файла совпадает с именеи директории dir
    '''
    dir = dir or Path.cwd()

    dir_stat = []

    def _walk_dir(cur_dir: str, stat: list[dict]) -> int:
        '''Рекурсивно обходит директорию cur_dir. Возвращает общий размер файлов в ней'''
        total_size = 0
        for obj in Path(cur_dir).iterdir():
            file_info = {}
            file_info['root'] = str(cur_dir)
            file_info['name'] = str(obj)
            is_dir = obj.is_dir()
            file_info['directory'] = is_dir
            is_file = obj.is_file()
            file_info['file'] = is_file
            if is_file:
                file_size = obj.stat().st_size
                file_info['size'] = file_size
                total_size += file_size
            elif is_dir:
                dir_size = _walk_dir(str(obj), dir_stat)
                total_size += dir_size
                file_info['size'] = dir_size
            stat.append(file_info)
        return total_size

    def _save_dir_stat(dir_stat: list[dict], dir: str) -> None:
        '''
        Сохраняет статистику по директории в файл указанного типа
        '''
        file_name = Path(dir).name
        file_name = f"{file_name}.{file_type.name.lower()}"
        match file_type:
            case FileType.JSON:
                s_json.write_json(dir_stat, file_name, preaty_print=True)
            case FileType.CSV:
                s_csv.write_ld_csv(dir_stat, file_name)
            case FileType.PICKLE:
                s_pickle.write_pickle(dir_stat, file_name)

    _walk_dir(dir, dir_stat)
    _save_dir_stat(dir_stat, dir)


if __name__ == '__main__':
    dir = Path.cwd() / 'tmp'
    get_dir_stat(dir, file_type=FileType.CSV)
