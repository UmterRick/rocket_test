from colorama import Fore
import re


def find_log(log_file: str, log_type: str = 'A', log_title: str = 'A'):
    """
    Функция поиска логов формата  YYYxxxxx<тип сообщения>. x - это цифра 0-9, Y - латинская буква A-Z из файла.
    :param log_title: Фильр записей по заголовкам типа YYY , Y - латинская буква A-Z
    :param log_file: имя файла в котором будет произведен поиск.
    :param log_type: Тип сообщения: E - ошибка, W - предупреждение, I - информационное сообщение.
    :return: Список словерей вида :
    {msg: "код ссобщения",
     type:"тип сообщения",
     offset:"смещение в байтах начала сообщения от начала файла",
     test:"текст сообщения"}
    """
    result = list()
    try:
        logs = open(log_file, 'r+')
        log_line = logs.readline()
    except OSError as err:
        print(Fore.RED + "Не удалось открыть файл" + err.filename)
        return list()

    while log_line:
        try:
            logs.tell()
            search = re.findall("\w\w\w\d\d\d\d\d\w", log_line[:10])
            if len(search) != 0:
                log_line = log_line.strip()
                if log_line[8] == log_type.upper() or log_type.upper() == "A":
                    if log_line[:3] == log_title.upper() or log_title.upper() == "A":
                        result.append({'msg': log_line[:8],
                                       'type': log_line[8],
                                       'offset': logs.tell(),
                                       'text': log_line[9:]})
            log_line = logs.readline()
        except OSError:
            print(Fore.RED + "Ошибка при поиске строки")
            return list()
        except IndexError:
            print(Fore.RED + "Ошибка получения данных строки")
            return list()
    return result


filename = input(Fore.CYAN + "Введите имя файла для поиска: ").strip()
print(Fore.WHITE)
for log in find_log('logs.txt', log_type='a', log_title='a'):
    print(log)
