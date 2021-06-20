import os
from colorama import Fore


def makepath(in_path: str):
    """
    Создние директорий используя строку содежащую полный путь каталогов
    :param in_path: Строка полного пути каталогов
    :return: True если указанные каталоги были созданы |
    False в случае неудачи
    """
    try:
        in_path = os.path.normpath(in_path)
        in_path = in_path.split(os.sep)
        if len(in_path) <= 1:
            print(Fore.RED + 'Путь к файлу указан некорректно')
            return False
        if in_path[0] == '':
            in_path.pop(0)
        layers = len(in_path)
    except TypeError:
        print(Fore.RED + 'Укажите корректный путь в строковом формате')
        return False

    parent = in_path.pop(0) + "\\"
    depth = 0

    while len(in_path) != 0:
        try:
            new_dir = in_path.pop(0)
            parent = os.path.join(parent, new_dir)
            os.mkdir(parent, 0o777)
            print(Fore.GREEN + f"Директория {new_dir} была создана в {parent}")
        except os.error as err:
            if err.errno == 17:
                print(Fore.YELLOW + f"Такая директория уже существует {err.filename}")
                depth += 1
                continue
            print(Fore.RED + err)
            return False
    if depth == (layers - 1):
        return False
    return True


path = fr"{input('Введите путь к директории:')}"
print(Fore.GREEN + "Путь был успешно создан") if makepath(path) else print(Fore.RED + "Ошибка при создании директорий")
