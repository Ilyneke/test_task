import logging

from .file import read
from .settings import FIELD_NAMES


SEARCH_MESSAGE = 'Введите номер поля по которому будет идти поиск или напишите menu для выхода в меню'
SEARCH_KEYWORD_MESSAGE = 'Введите текст по которому будет идти поиск:'
NOT_FOUND_MESSAGE = '\nНе удалось найти записи, попробуйте еще раз с другими данными\n'


def _show_fields() -> None:
    """Вывод полей для выбора"""
    print()
    for i, field in enumerate(FIELD_NAMES):
        print(i, field)


def _search_in_field(data: list[dict], field: str, search_keyword: str, width: dict) -> list[dict]:
    """Поиск записей по ключевому слову (строке)"""
    founded = []
    for i, row in enumerate(data):
        if search_keyword in row[field]:
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
    print(SEARCH_MESSAGE)
    field_number = input()
    while not (field_number.isdigit() and 0 <= int(field_number) <= len(FIELD_NAMES) - 1):
        if field_number == 'menu':
            return
        field_number = input()
    field = FIELD_NAMES[int(field_number)]
    print(SEARCH_KEYWORD_MESSAGE)
    search_keyword = input()
    width = {}
    founded = _search_in_field(data=data, field=field, search_keyword=search_keyword, width=width)
    if founded:
        _show(rows=founded, width=width)
    else:
        logging.info(NOT_FOUND_MESSAGE)
        search()
