from pathlib import Path
from enum import Enum
import serialize.s_json as s_json
import serialize.s_csv as s_csv
import serialize.s_pickle as s_pickle
import argparse
from mylog import init_logging


class FileType(Enum):
    JSON = 1
    CSV = 2
    PICKLE = 3
    NONE = 4


def _parse_arg() -> tuple[str, FileType]:
    """Распаривает аргументы для сбора статистики по дирректори"""

    parser = argparse.ArgumentParser(
        description="Сбор статистики по директории со всеми поддиректориями"
    )

    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        default=Path.cwd(),
        help="Директория для обхода. (По умолчанию - текущая)",
    )

    ser_types = [val._name_.lower() for val in FileType]

    parser.add_argument(
        "-s",
        "--serialize-file",
        default="none",
        choices=ser_types,
        help="Тип файла для сохранения результата обхода. (По умолчанию none - сохранять не надо)",
    )

    args = parser.parse_args()
    serType = FileType(ser_types.index(args.serialize_file) + 1)
    return (args.dir, serType)


def get_dir_stat(dir: str = "", file_type: FileType = FileType.NONE) -> None:
    """
    Собирает статистику по директории dir c учетом вложенности и записывает
    результат в файлы формата json, csv, pickle. Имя файла совпадает с именеи директории dir
    """

    logger = init_logging("dir_stat")

    dir = dir or Path.cwd()

    dir_stat = []

    def _walk_dir(cur_dir: str, stat: list[dict]) -> int:
        """Рекурсивно обходит директорию cur_dir. Возвращает общий размер файлов в ней"""

        total_size = 0

        for obj in Path(cur_dir).iterdir():
            file_info = {}
            file_info["root"] = str(cur_dir)
            file_info["name"] = str(obj)
            is_dir = obj.is_dir()
            file_info["directory"] = is_dir
            is_file = obj.is_file()
            file_info["file"] = is_file
            if is_file:
                file_size = obj.stat().st_size
                file_info["size"] = file_size
                total_size += file_size
            elif is_dir:
                dir_size = _walk_dir(str(obj), dir_stat)
                total_size += dir_size
                file_info["size"] = dir_size
            stat.append(file_info)
            logger.info(f"{file_info}")
        return total_size

    def _save_dir_stat(dir_stat: list[dict], dir: str) -> None:
        """
        Сохраняет статистику по директории в файл указанного типа
        """
        file_name = Path(dir).name
        file_name = f"{file_name}.{file_type.name.lower()}"
        match file_type:
            case FileType.JSON:
                s_json.write_json(dir_stat, file_name, preaty_print=True)
            case FileType.CSV:
                s_csv.write_ld_csv(dir_stat, file_name)
            case FileType.PICKLE:
                s_pickle.write_pickle(dir_stat, file_name)

    logger.info(f"Start directory {dir} traversal")
    try:
        _walk_dir(dir, dir_stat)
    except Exception as er:
        logger.error(er)
        print(
            f"Какая-то ошибка. Детали смотрите в файле - {logger.handlers[0].baseFilename}"
        )
    else:
        logger.info(f"Stop directory {dir} traversal")

        if file_type != FileType.NONE:
            _save_dir_stat(dir_stat, dir)
            logger.info(f"Data serialized to {Path(dir).name}.{file_type.name.lower()}")


def dir_stat() -> None:
    dir, file_type = _parse_arg()
    get_dir_stat(dir, file_type)


if __name__ == "__main__":
    dir_stat()
