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
    DEFAULT_FILE_NAME = 'unnamed'

    def serialize(self, data: Any, file_name: str) -> None:
        '''
        Сериализует данные data в файл file_name
        '''
        if not file_name:
            file_name = self.DEFAULT_FILE_NAME
        self._file_name = '.'.join(
            (file_name, self.FILE_TYPE.name.lower())) if Path(file_name).suffix == '' else file_name

    def deserialize(self, file: str) -> Any:
        '''
        Десериализует данные из файла file
        '''
        pass
