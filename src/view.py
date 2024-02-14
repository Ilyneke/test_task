import os

from .settings import FIELD_NAMES, MENU, COMMAND_PROMPT
from .file import read


VIEW_MESSAGE = 'Нажмите Enter для продолжения или наберите menu для выхода в меню:'


def _get_terminal_lines() -> int:
    """Функция возвращает количество помещаемых строк в консоли, работает только на linux"""
    if os.name == 'posix':
        try:
            return os.get_terminal_size().lines
        except OSError:
            return 12
    else:
        return 12


def _get_max_widths(rows: list) -> dict:
    """Функция возвращает словарь из названий полей и максимальной шириной значения, нужно для красивого отображения"""
    width = {field: len(field) for field in FIELD_NAMES}
    for row in rows:
        width = {field: max(width[field], len(row[field])) for field in FIELD_NAMES}
    return width


def _get_header(len_rows: int, width: dict) -> str:
    """Функция формирует строку из названий столбцов в зависимости от максимальной ширины значений"""
    num = '№'.ljust(len(str(len_rows)) + 1)
    header = num + ' '.join([field.ljust(width[field]) for field in FIELD_NAMES])
    return header


def _get_formatted_row(row: dict, width: dict, len_rows: int, num: int) -> str:
    """Функция формирует строку из значений записи, аналогично _get_header()"""
    num = str(num).ljust(len(str(len_rows)) + 1)
    formatted = num + ' '.join([row[field].ljust(width[field]) for field in FIELD_NAMES])
    return formatted


def show() -> None:
    """Постраничный вывод записей из справочника"""
    data = read()
    if not data:
        return
    count_lines = _get_terminal_lines() - 4
    print(f'COUNT LINES: {count_lines}')
    widths = _get_max_widths(rows=data)
    header = _get_header(len_rows=len(data), width=widths)
    printed = 0
    page = 1
    print(header)
    for row in data:
        formatted_row = _get_formatted_row(row=row, width=widths, len_rows=len(data), num=printed)
        print(formatted_row)
        printed += 1
        if printed > count_lines * page + (page - 1):
            print(VIEW_MESSAGE)
            command = input(COMMAND_PROMPT)
            if not command:
                print(header)
                page += 1
            elif command == 'menu':
                return
    empty_lines = '\n' * (count_lines - printed % count_lines - len(MENU) + (page - 1))
    print(empty_lines)
