from typing import Any
from enum import Enum
from pathlib import Path


class FileType(Enum):
    CSV = 1
    JSON = 2
    PICKLE = 3


class Serializer:
    '''
    Базовый класс 
    '''
    FILE_TYPE: FileType = None

    def __init__(self, file_name: str) -> None:
        self._file_name = '.'.join(
            (file_name, self.FILE_TYPE.name.lower())) if Path(file_name).suffix == '' else file_name

    def serialize(self, data: Any) -> None:
        '''
        Сериализует данные data в файл file_name
        '''
        pass

    def deserialize(self) -> Any:
        '''
        Десериализует данные из файла file_name
        '''
        pass
