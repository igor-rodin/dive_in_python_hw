import os


def run_tests():
    print(" Запуск тестов ".center(80, "="))
    print("1 - Doctest\n2 - Unittest\n3 - Pytest")
    test_type = int(input("> "))
    match test_type:
        case 1:
            os.system("python -m doctest -v student.py")
        case 2:
            os.system("python -m unittest -v tests/test_student_unittest.py")
        case 3:
            os.system("python -m pytest -vv tests/test_student_pytest.py")


if __name__ == "__main__":
    run_tests()
