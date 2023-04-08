'''Сериалайзер в pickle формат'''

import pickle
from typing import Any
from serialize.serializer import Serializer, FileType


class PickleSerializer(Serializer):
    FILE_TYPE = FileType.PICKLE

    def __save_file(self, data: Any) -> None:
        '''
        Сериализует объект data в pickle_file
        '''
        with open(self._file_name, 'wb') as f:
            pickle.dump(data, f, protocol=pickle.DEFAULT_PROTOCOL)

    def __save_str(self, data: Any) -> bytes:
        '''
        Сериализует объект data в pickle строку
        '''
        return pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)

    def __read_file(self, file: str) -> Any:
        with open(file, mode='rb') as f:
            data = pickle.load(f)
        return data

    def __read_bytes(self, file: str) -> Any:
        return pickle.loads(file)

    def serialize(self, data: Any, file_name: str = '', as_bytes=False) -> None | bytes:
        '''
        Сериализует объект data в pickle формате
        '''

        super().serialize(data, file_name)

        if not as_bytes:
            self.__save_file(data)
        else:
            return self.__save_str(data)

    def deserialize(self, file: str | bytes, as_bytes=False) -> Any:
        '''
        Десериализует данные из источника данных file в pickle формате
        '''
        if not as_bytes:
            return self.__read_file(file)
        else:
            return self.__read_bytes(file)
