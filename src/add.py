import logging

from .settings import FIELD_NAMES
from .file import write


NEW_MESSAGE = f'Введите новые данные в формате:\n{", ".join(FIELD_NAMES)}\n'
SUCCESS_MESSAGE = 'Запись добавлена'


def new() -> None:
    """Добавление записи в справочник"""
    row = input(NEW_MESSAGE)
    row = [elem.strip() for elem in row.split(',')]
    write(row)
    logging.info(SUCCESS_MESSAGE)
