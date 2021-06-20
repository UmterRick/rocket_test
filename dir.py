import os


def makepath(path: str):
    try:
        path = os.path.normpath(path)
        path = path.split(os.sep)
        if len(path) <= 1:
            print('Путь к файлу указан некорректно')
            return -1
        if path[0] == '':
            path.pop(0)
    except TypeError:
        print('Укажите корректный путь в строковом формате')
        return -1

    parent = path.pop(0) + "\\"
    while len(path) != 0:
        try:
            new_dir = path.pop(0)
            parent = os.path.join(parent, new_dir)
            os.mkdir(parent, 0o777)
        except os.error as err:
            if err.errno == 17:
                print(f"Такой файл уже существует {err.filename}")
                continue
            print(err)
            return -1
    return 1
