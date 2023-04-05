''' Содержит функции декораторы для логировния в json и подстановки параметров из csv файлов
    При инициализации пакета генерируются параметры уравнения
'''

__all__ = ['log_json', 'param_csv']

from param_generator import gen_params_csv

gen_params_csv(count=100)
