# Задание №1
# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.


from typing import Any
import json


def get_number(message: str) -> int | float:
    while True:
        try:
            data = input(message)
            return int(data)
        except ValueError:
            try:
                return float(data)
            except ValueError:
                print("Должно быть целое или вещественное")


# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get(dct: dict, key: Any, default: Any) -> Any:
    try:
        val = dct[key]
    except KeyError:
        val = default

    return val


# Задание №3
# Создайте класс с базовым исключением и дочерние классы исключения:
# - ошибка уровня,
# - ошибка доступа.


class UserExeption(Exception):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id


class LevelError(UserExeption):
    def __init__(self, user_id: int, level: int) -> None:
        super().__init__(user_id)
        self.level = level

    def __str__(self) -> str:
        return f"Уровень {self.level} пользователя с id: {self.user_id} недостаточен для входа"


class AccesError(UserExeption):
    def __init__(self, user_id: int, user_name: str) -> None:
        super().__init__(user_id)
        self.user_name = user_name

    def __str__(self) -> str:
        return f"Пользоветель {self.user_name} c id {self.user_id} не существует"


# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.


class User:
    def __init__(self, name: str, user_id: int, level: int) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, __value: object) -> bool:
        if self is __value:
            return True
        if type(__value) is not User:
            return False

        return self.name == __value.name and self.user_id == __value.user_id

    def __hash__(self) -> int:
        return hash((self.name, self.user_id, self.level))

    def __str__(self) -> str:
        return f"User: {self.name}, id: {self.user_id}, level: {self.level}"


def get_users(file_json: str) -> set[User]:
    user_data = None
    with open(file_json, mode="r", encoding="utf-8") as f:
        user_data = json.load(f)

    users = []
    for data in user_data:
        for key, val in data.items():
            tmp = [
                User(user_name, user_id, int(key)) for user_name, user_id in val.items()
            ]
            users.extend(tmp)
    return set(users)


# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
#  - загрузка данных (функция из задания 4)
#  - вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
#   магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа.
#   А если пользователь есть, получите его уровень из множества пользователей.
# - добавление пользователя. Если уровень пользователя
#   меньше, чем ваш уровень, вызывайте исключение уровня доступа.


class UserManagement:
    _users_file: str = None
    _users: set[User] = set()
    _logged_user: User = None

    def __init__(self, users_file: str) -> None:
        self._users_file = users_file
        self.__load()

    def __load(self):
        user_data = None
        with open(self._users_file, mode="r", encoding="utf-8") as f:
            user_data = json.load(f)

        for data in user_data:
            for key, val in data.items():
                tmp = (
                    User(user_name, user_id, int(key))
                    for user_name, user_id in val.items()
                )
                self._users.update(tmp)

    def login(self, user_name: str, user_id: int) -> None:
        tmp = User(user_name, user_id, 0)

        for user in self._users:
            if user == tmp:
                self._logged_user = user
                return

        raise AccesError(user_id, user_name)

    def register(self, user_name: str, user_id: int, level: int) -> None:
        if self._logged_user.level != level:
            raise LevelError(user_id, level)

        self._users.update(User(user_name, user_id, level))


# Задание №6
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

if __name__ == "__main__":
    # num = get_number("Введите целое или вещественное число: ")
    # print(f"{num=}")

    # dct = {"a": 2, "c": 4}

    # print(f'{get(dct, "a", 0)=}')
    # print(f'{get(dct, "d", 0)=}')
    # raise LevelError()
    # raise AccesError()

    # for user in get_users("users.json"):
    #     print(user)

    management = UserManagement("users.json")
    try:
        management.login("User_1", 4)
    except AccesError as e:
        print(e)
    else:
        print(f"{management._logged_user}")
