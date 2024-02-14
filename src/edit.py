import logging

from .file import read, just_read_list, rewrite
from .settings import NOT_FOUND_MESSAGE, FIELD_NAMES


START_EDIT_MESSAGE = 'Введите номер записи, которую хотите отредактировать '
ERROR_VALIDATION_MESSAGE = 'Данные введены некорректно, попробуйте еще раз'
ERROR_NUMBER_MESSAGE = 'Записи под таким номером нет, попробуйте ввести еще раз'
EDIT_MESSAGE = (f'Введите новые данные в формате:\n'
                f'{", ".join(FIELD_NAMES)}\n'
                f'если хотите оставить поле таким же, то напишите в нем "/s":')


def _print_chosen_row(row: dict) -> None:
    """Вывод выбранной записи"""
    print()
    widths = {field: max(len(field), len(row[field])) for field in FIELD_NAMES}
    header = ' '.join([field.ljust(widths[field]) for field in FIELD_NAMES])
    print(header)
    row = ' '.join([row[field].ljust(widths[field]) for field in FIELD_NAMES])
    print(row, end='\n')


def _validate(row: str) -> bool:
    """Проверка ввода пользователя"""
    values = row.split(',')
    if len(values) == len(FIELD_NAMES):
        return True
    return False


def _update(num: int, old: dict, new: str) -> str:
    """Сохранение изменений"""
    new_row = [elem.strip() for elem in new.split(',')]
    new_values = []
    for i in range(len(old.keys())):
        if new_row[i] != '/s':
            new_values.append(new_row[i])
        else:
            new_values.append(list(old.values())[i])
    data = just_read_list()
    if data:
        data[num] = new_values
        rewrite(data)
        return ', '.join(new_values)


def edit() -> None:
    """Редактирование записей"""
    data = read()
    if not data:
        logging.warning(NOT_FOUND_MESSAGE)
        return
    start_edit_message = START_EDIT_MESSAGE + f'[0-{len(data)}]'
    print(start_edit_message)
    num = input()
    while not (num.isdigit() and 0 <= int(num) <= len(data)):
        logging.warning(ERROR_NUMBER_MESSAGE)
        num = input()
    num = int(num) - 1
    _print_chosen_row(data[num])
    print(EDIT_MESSAGE)
    new_row = input()
    while not _validate(new_row):
        logging.warning(ERROR_VALIDATION_MESSAGE)
        new_row = input()
    new = _update(num=num, old=data[num], new=new_row)
    logging.info(f'Измененная запись сохранена!:\n{new}')
