import os
import csv

from .settings import FIELD_NAMES
from .file import read


def _get_terminal_lines() -> int:
    if os.name == 'posix':
        return os.get_terminal_size().lines
    else:
        return 12


def _get_max_widths(rows) -> dict:
    width = {field: len(field) for field in FIELD_NAMES}
    for row in rows:
        width = {field: max(width[field], len(row[field])) for field in FIELD_NAMES}
    return width


def _to_dict(reader: csv.DictReader) -> list:
    print(reader)
    result = []
    for row in reader:
        result.append(row.__dict__)
    return result


def show() -> None:
    lines = _get_terminal_lines()

    reader_data = read()
    data = _to_dict(reader_data)

    printed = 0
    lines_all = 0
    widths = _get_max_widths(rows=data)
    print(*FIELD_NAMES, sep='\t')
    print('№'.ljust(len(str(lines_all)) + 1) + ' '.join(
        [field.ljust(widths[field]) for field in FIELD_NAMES]
    ))

    page = 0
    for row in data:
        printed += 1
        print(str(printed).ljust(len(str(lines_all)) + 1) + ' '.join(
            [row[field].ljust(widths[field]) for field in FIELD_NAMES])
              )
        if printed - page * lines > lines - 3 - bool(page) * 2:
            command = input('Нажмите Enter для продолжения или наберите menu для выхода в меню: ')
            if not command:
                page += 1
                print('№'.ljust(len(str(lines_all)) + 1) + ' '.join(
                    [field.ljust(widths[field]) for field in FIELD_NAMES]
                ))
            elif command == 'menu':
                return
