import logging

from .file import read
from .settings import FIELD_NAMES, COMMAND_PROMPT


SEARCH_MESSAGE = 'Введите номер поля по которому будет идти поиск или напишите menu для выхода в меню'
SEARCH_KEYWORD_MESSAGE = 'Введите текст по которому будет идти поиск:'
ANOTHER_KEYWORD_MESSAGE = ('Чтобы начать искать по выбранным данным нажмите enter, чтобы добавить еще один критерий '
                           'напишите add: ')
NOT_FOUND_MESSAGE = 'Не удалось найти записи, попробуйте еще раз с другими данными\n'


def _show_fields() -> None:
    """Вывод полей для выбора"""
    print()
    for i, field in enumerate(FIELD_NAMES):
        print(i, field)


def _search_in_field(data: list[dict], search_data: dict, width: dict) -> list[dict]:
    """Поиск записей по ключевому слову (строке)"""
    founded = []
    for i, row in enumerate(data):
        if all([search_data[key] in row[key] for key in search_data.keys()]):
            row['id'] = i
            founded.append(row)
            for key, value in row.items():
                width[key] = max(width.get(key, 0), len(str(value)) + 1)
    return founded


def _show(rows: list[dict], width: dict) -> None:
    """Вывод найденных записей"""
    header = '№'.ljust(width['id']) + ''.join([field.ljust(width[field]) for field in FIELD_NAMES])
    print()
    logging.info(f'Найдено {len(rows)} записей:')
    print(header)
    for row in rows:
        row = str(row['id']).ljust(width['id']) + ''.join([row[field].ljust(width[field]) for field in FIELD_NAMES])
        print(row)
    print()


def search():
    """Функция для поиска записей"""
    data = read()
    _show_fields()
    search_data = {}
    for _ in range(len(FIELD_NAMES)):
        print(SEARCH_MESSAGE)
        field_number = input(COMMAND_PROMPT)
        while not (field_number.isdigit() and 0 <= int(field_number) <= len(FIELD_NAMES) - 1):
            if field_number == 'menu':
                return
            field_number = input(COMMAND_PROMPT)
        field = FIELD_NAMES[int(field_number)]
        print(SEARCH_KEYWORD_MESSAGE)
        search_keyword = input(COMMAND_PROMPT)
        search_data[field] = search_keyword
        print(ANOTHER_KEYWORD_MESSAGE)
        command = input(COMMAND_PROMPT)
        if command != 'add':
            break
    width = {}
    founded = _search_in_field(data=data, search_data=search_data, width=width)
    if founded:
        _show(rows=founded, width=width)
    else:
        logging.info(NOT_FOUND_MESSAGE)
        search()
