import os

from .settings import FIELD_NAMES, MENU
from .file import read


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
    count_lines = _get_terminal_lines() - 2
    widths = _get_max_widths(rows=data)
    header = _get_header(len_rows=len(data), width=widths)
    print(header)
    printed = 0
    page = 1
    for row in data:
        printed += 1
        formatted_row = _get_formatted_row(row=row, width=widths, len_rows=len(data), num=printed)
        print(formatted_row)
        if printed > count_lines * page - 1:
            command = input('Нажмите Enter для продолжения или наберите menu для выхода в меню: ')
            if not command:
                page += 1
                print(header)
            elif command == 'menu':
                return
    empty_lines = '\n' * (count_lines - printed % count_lines - len(MENU) - 2)
    print(empty_lines)
