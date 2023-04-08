'''Сериалайзер в csv формат'''

import csv
from typing import Any
from serialize.serializer import Serializer, FileType


class CsvSerializer(Serializer):
    FILE_TYPE = FileType.CSV

    def __save_ld(self, data: list[dict]) -> None:
        '''
        Записывает в csv_file список словарей data 
        '''
        with open(self._file_name, 'w', newline='', encoding='utf-8') as f:
            header = [key for key in data[0].keys()]
            csv_write = csv.DictWriter(
                f, fieldnames=header, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            csv_write.writeheader()
            csv_write.writerows(data)

    def __save_l(self, data: Any) -> None:
        '''
        Записывает в csv_file список с произвольными данными 
        '''
        if not isinstance(data, list):
            data = [data]

        with open(self._file_name, mode='w', newline='', encoding='utf-8') as f_csv:
            csv_w = csv.writer(f_csv, dialect='excel',
                               quoting=csv.QUOTE_NONNUMERIC)
            csv_w.writerows(data)

    def __read_l(self, file: str) -> list:
        '''
        Возвращает из csv_file список
        '''
        with open(file, mode='r', encoding='utf-8', newline='') as f:
            csv_read = csv.reader(f, dialect='excel',
                                  quoting=csv.QUOTE_NONNUMERIC)
            data = []
            for i, row in enumerate(csv_read):
                if i != 0:
                    data.append(row)
        return data

    def __read_ld(self, file: str) -> list:
        '''
        Возвращает из csv_file список словарей
        '''
        with open(file, mode='r', encoding='utf-8', newline='') as f:
            csv_read = csv.DictReader(f, dialect='excel',
                                      quoting=csv.QUOTE_NONNUMERIC)
            data = []
            for i, row in enumerate(csv_read):
                data.append(row)
        return data

    def serialize(self, data: Any, file_name: str) -> None:
        '''
        Сериализует данные data в файл file_name
        '''
        super().serialize(data, file_name)

        if isinstance(data, list) and isinstance(data[0], dict):
            self.__save_ld(data)
        else:
            self.__save_l(data)

    def deserialize(self, file: str, as_dict=True) -> Any:
        '''
        Десериализует данные из файла file_name. Возвращает список словарей, если as_dict == True
        '''
        data = []
        if as_dict:
            data = self.__read_ld(file)
        else:
            data = self.__read_l(file)

        return data
