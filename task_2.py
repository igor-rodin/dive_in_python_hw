
def name_prize(names: list[str], salares: list[int], interest_prize: list[str]) -> dict[str, float]:
    '''
    Возвращает словарь с именем в качестве ключа и суммой премии в качестве значения
    '''
    return {name: salary * float(interest[:-1])*0.01 for name, salary, interest in zip(names, salares, interest_prize)}


names = ['emp_1', 'emp_2', 'emp_3', 'emp_4', 'emp_5']
salares = [1000, 2500, 1300, 5000, 10000]
interest_prize = ['10.25%', '15.0%', '10.0%', '20.0%', '5.0%']

print(f"Prizes: {name_prize(names, salares, interest_prize)}")
