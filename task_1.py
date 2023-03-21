import os


def path_info(abs_path: str) -> tuple((str, str, str)):
    '''
    Возвращает кортеж из трёх элементов: путь, имя файла, расширение файла
    '''

    (*path, file_name) = abs_path.split(os.sep)
    i = file_name.rfind('.')
    (file_name, file_ext) = (
        file_name[:i], file_name[i+1:]) if i > -1 else (file_name, '')
    path = f'{os.sep}'.join(path) if len(path) > 1 else os.sep

    return (path, file_name, file_ext)


abs_path = "/Users/igor-rodin/work/gb/dive_in_python/homeworks/task_1.py"
abs_path_2 = "/.my_file.txt"
abs_path_3 = "/opt/homebrew/bin/python3"

path, file_name, file_ext = path_info(abs_path_2)

print(f"{abs_path_2= }\n")
print(f"{path= }")
print(f"{file_name= } ")
print(f"{file_ext= }")
