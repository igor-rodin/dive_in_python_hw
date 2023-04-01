'''Задачи с семинара'''

from pathlib import Path
import os
import serialize.s_json as s_json
import serialize.s_csv as s_csv
import serialize.s_pickle as s_pickle
import csv


# Задание No1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.


def names_json(txt_file: str, json_file: str) -> None:
    with(
        open(txt_file, 'r', encoding='utf-8') as f_txt,
        open(json_file, 'w', encoding='utf-8') as f_json
    ):
        all_data = {}
        while data := f_txt.readline():
            name, number = data[:-1].split()
            number = int(number) if number.find('.') == -1 else float(number)
            all_data[name.capitalize()] = number
        json.dump(all_data, f_json, ensure_ascii=False, indent=4)


# Задание No2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа(от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию вJSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

def get_user_info(json_file: str) -> None:
    used_ids = set()
    levels = set(range(1, 8))
    users = {}

    if Path(Path.cwd() / json_file).is_file():
        users = s_json.read_json(json_file)

    used_ids = {int(id) for _, val in users.items() for _, id in val.items()}

    while True:
        input_data = input(
            'Введите через пробел: имя идентификатор "уровень доступа"> ')
        if input_data == '':
            break

        user_name, user_id, user_level = input_data.split()
        user_id = int(user_id)

        while user_id in used_ids:
            print("Пользователь с таким id уже существует")
            user_name, user_id, user_level = input(
                'Введите через пробел: имя идентификатор "уровень доступа"> ').split()
        else:
            used_ids.add(id)

        user_level = int(user_level)
        while user_level not in levels:
            print(f"Уровень доступа {user_level} не существует")
            user_name, user_id, user_level = input(
                'Введите через пробел: имя идентификатор "уровень доступа"> ').split()

        users.setdefault(user_level, {})[user_name] = user_id
        s_json.write_json(users, json_file)


# Задание No3
# 📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

def user_to_scv(json_file: str, csv_file: str) -> None:
    users = s_json.read_json(json_file)

    csv_data = [(int(user_id), name, int(level)) for level, user in users.items()
                for name, user_id in user.items()]
    s_csv.write_l_csv(csv_data, csv_file)

# Задание No4
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.


def new_users(csv_file: str, json_file: str) -> None:
    with open(csv_file, mode='r', newline='', encoding='utf-8') as f_csv:
        csv_read = csv.reader(f_csv, dialect='excel')
        al_data = []
        for row in csv_read:
            user = {}
            user['id'] = f"{row[0]:0>10}"
            user['name'] = row[1].capitalize()
            user['level'] = row[2]
            user['hash'] = hash(f"{user['id']}{user['name']}")
            al_data.append(user)

    s_json.write_json(al_data, json_file)


# Задание No5
# 📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.

def json_to_pickle(dir: str) -> None:
    ext_from = 'json'
    ext_to = 'pickle'
    os.chdir(dir)
    for file in Path(Path.cwd()).iterdir():
        if file.match(f'*.{ext_from}'):
            data = s_json.read_json(file.name)
            file_name, _ = file.name.split('.')
            pickle_file = f"{file_name}.{ext_to}"
            s_pickle.write_pickle(data, pickle_file)

# Задание No6
# 📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.


def pickle_to_csv(pickle_file: str, csv_file: str) -> None:
    list_data = read_pickle(pickle_file)
    write_ld_csv(list_data, csv_file)


# Задание No7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

def csv_to_pickles(csv_file: str) -> None:
    data = s_csv.read_l_csv(csv_file)
    pickle_str = s_pickle.write_pickles(data)
    print(f'{pickle_str=}')


if __name__ == '__main__':
    # names_json('data_prod.txt', 'prod.json')
    # get_user_info('users.json')
    # user_to_scv('users.json', 'users.csv')
    # new_users('users.csv', 'users_new.json')
    dir = Path.cwd()
    # json_to_pickle(dir)
    pickle_file = 'users_new.pickle'
    # pickle_to_csv(pickle_file, 'pickle_to_csv.csv')
    csv_to_pickles('pickle_to_csv.csv')
