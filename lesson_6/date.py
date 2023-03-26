from sys import argv

'''
Содержит функции для проверки коррекиности даты в диапазоне лет [1, 9999]
'''
__all__ = ['check_date']

__LOW_LIMIT_YEAR = 1
__UPPER_LIMIT_YEAR = 9999
__DEFAULT_DATE = "01.01.01"

__month_days_31 = {1, 3, 5, 7, 8, 10, 12}
__month_days_30 = {2, 4, 6, 9, 11}
__month_days_28_or_29 = 2


def __is_leep_year(year: int) -> bool:
    '''
    Проверяет, является ли год високосным
    '''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def check_date(date: str) -> bool:
    '''
    Проверяет, существует ли дата, заданная в формате "dd.mm.yyyy"
    '''
    day, month, year = map(int, date.split('.'))

    if year < __LOW_LIMIT_YEAR or year > __UPPER_LIMIT_YEAR:
        return False
    if month not in __month_days_30 and month not in __month_days_31:
        return False
    if month in __month_days_31 and day not in range(1, 32):
        return False
    if month in __month_days_30 and day not in range(1, 31):
        return False

    if month == __month_days_28_or_29:
        return day in range(1, 30) if __is_leep_year(year) else day in range(1, 29)

    return True


if __name__ == '__main__':
    date = argv[1] if len(argv) > 1 else __DEFAULT_DATE
    print(check_date(date))
