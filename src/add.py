import logging

from .settings import FIELD_NAMES, COMMAND_PROMPT
from .file import write


NEW_MESSAGE = f'Введите новые данные в формате:\n{", ".join(FIELD_NAMES)}'
SUCCESS_MESSAGE = 'Запись добавлена'


def new() -> None:
    """Добавление записи в справочник"""
    print(NEW_MESSAGE)
    row = input(COMMAND_PROMPT)
    row = [elem.strip() for elem in row.split(',')]
    write(row)
    logging.info(SUCCESS_MESSAGE)
