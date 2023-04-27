'''Содержит функции для сериализации(десеарилизации) в формат csv'''

import csv

__all__ = ['write_ld_csv', 'write_l_csv', 'read_l_csv']


def write_ld_csv(data: list[dict], csv_file: str) -> None:
    '''
    Записывает в csv_file список словарей data 
    '''
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        header = [key for key in data[0].keys()]
        csv_write = csv.DictWriter(
            f, fieldnames=header, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


def write_l_csv(data: list, csv_file: str) -> None:
    '''
    Записывает в csv_file список с произвольными данными 
    '''
    with open(csv_file, mode='w', newline='', encoding='utf-8') as f_csv:
        csv_w = csv.writer(f_csv, dialect='excel',
                           quoting=csv.QUOTE_NONNUMERIC)
        csv_w.writerows(data)


def read_l_csv(csv_file: str) -> list:
    '''
    Возвращает из csv_file список
    '''
    with open(csv_file, mode='r', encoding='utf-8', newline='') as f:
        csv_read = csv.reader(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        data = []
        for i, row in enumerate(csv_read):
            if i != 0:
                data.append(row)
    return data
