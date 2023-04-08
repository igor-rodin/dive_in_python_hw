'''Сериалайзер в json формат'''

import json
from typing import Any, Sequence
from serialize.serializer import Serializer, FileType


class JsonSerializer(Serializer):
    FILE_TYPE = FileType.JSON

    def serialize(self, data: Any, file_name: str, preaty_print=False) -> None:
        '''
        Записывает в файл json_file объект data
        '''
        super().serialize(data, file_name)

        if not isinstance(data, Sequence) and not isinstance(data, dict):
            data = [data]

        with open(self._file_name, mode='w', encoding='utf-8') as f:
            indent_size = 2 if preaty_print else None
            json.dump(data, f, ensure_ascii=False, indent=indent_size)

    def deserialize(self, file: str) -> Any:
        '''
        Десериализует данные из файла file_name. Возвращает список словарей, если as_dict == True
        '''
        with open(file, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data
