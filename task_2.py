def dict_from_args(**kvargs) -> dict[str | float | int, str]:
    '''
    Возвращает словарь, где ключ — значение переданного аргумента, а значение — имя аргумента
    '''
    result = dict()
    for key, value in kvargs.items():
        try:
            hash(value)
        except TypeError:
            value = str(value)
        result.setdefault(value, []).append(key)
    return result


res = dict_from_args(length=1, width=1, weight=3.2, title="Help",
                     set={1, 2, 3}, dict={'w': 2, 'f': 0})

print(f"{res= }")
